# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016: Alignak contrib team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak contrib projet.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.

import os
import shlex
import time
import subprocess
import json
import unittest2
from alignak_module_backend.arbiter.module import AlignakBackendArbiter
from alignak_module_backend.broker.module import AlignakBackendBroker
from alignak.objects.host import Host
from alignak.objects.service import Service
from alignak.objects.contact import Contact
from alignak.objects.module import Module
from alignak_backend_client.client import Backend

from alignak.brok import Brok

class TestBrokerStatusUpdate(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set test mode for alignak backend
        os.environ['TEST_ALIGNAK_BACKEND'] = '1'
        os.environ['ALIGNAK_BACKEND_MONGO_DBNAME'] = 'alignak-module-backend-update-status'

        # Delete used mongo DBs
        print ("Deleting Alignak backend DB...")
        exit_code = subprocess.call(
            shlex.split(
                'mongo %s --eval "db.dropDatabase()"' % os.environ[
                    'ALIGNAK_BACKEND_MONGO_DBNAME'])
        )
        assert exit_code == 0

        cls.p = subprocess.Popen(['uwsgi', '--plugin', 'python', '-w', 'alignakbackend:app',
                                  '--socket', '0.0.0.0:5000',
                                  '--protocol=http', '--enable-threads', '--pidfile',
                                  '/tmp/uwsgi.pid'])
        time.sleep(3)

        cls.backend = Backend('http://127.0.0.1:5000')
        cls.backend.login("admin", "admin", "force")
        realms = cls.backend.get_all('realm')
        for cont in realms['_items']:
            cls.realm_all = cont['_id']

        timeperiods = cls.backend.get_all('timeperiod')
        for tp in timeperiods['_items']:
            if tp['name'] == '24x7':
                timeperiods_id = tp['_id']

        # add commands
        data = json.loads(open('cfg/command_ping.json').read())
        data['_realm'] = cls.realm_all
        data_cmd_ping = cls.backend.post("command", data)
        data = json.loads(open('cfg/command_http.json').read())
        data['_realm'] = cls.realm_all
        data_cmd_http = cls.backend.post("command", data)

        # add user
        data = {'name': 'jeronimo', 'host_notification_period': timeperiods_id,
                'service_notification_period': timeperiods_id, '_realm': cls.realm_all}
        data_user_jeronimo = cls.backend.post("user", data)

        # add usergroup
        data = {'name': 'admins', '_realm': cls.realm_all, 'users': [data_user_jeronimo['_id']]}
        data_usergroup = cls.backend.post("usergroup", data)

        # add host template
        data = json.loads(open('cfg/host_srvtemplate.json').read())
        data['check_command'] = data_cmd_ping['_id']
        del data['realm']
        data['_realm'] = cls.realm_all
        cls.data_host = cls.backend.post("host", data)

        # add host
        data = json.loads(open('cfg/host_srv001.json').read())
        data['check_command'] = data_cmd_ping['_id']
        del data['realm']
        data['_realm'] = cls.realm_all
        data['users'] = [data_user_jeronimo['_id']]
        data['usergroups'] = [data_usergroup['_id']]
        cls.data_host = cls.backend.post("host", data)

        # Add hostgroup
        data = {'name': 'allmyhosts', '_realm': cls.realm_all, 'hosts': [cls.data_host['_id']]}
        cls.data_hostgroup = cls.backend.post("hostgroup", data)

        # add service ping
        data = json.loads(open('cfg/service_srv001_ping.json').read())
        data['host'] = cls.data_host['_id']
        data['check_command'] = data_cmd_ping['_id']
        data['_realm'] = cls.realm_all
        data['users'] = [data_user_jeronimo['_id']]
        data['usergroups'] = [data_usergroup['_id']]
        cls.data_srv_ping = cls.backend.post("service", data)

        # add service pong
        data = json.loads(open('cfg/service_srv001_pong.json').read())
        data['host'] = cls.data_host['_id']
        data['check_command'] = data_cmd_ping['_id']
        data['_realm'] = cls.realm_all
        data['users'] = [data_user_jeronimo['_id']]
        data['usergroups'] = [data_usergroup['_id']]
        data['hostgroups'] = [cls.data_hostgroup['_id']]
        cls.data_srv_pong = cls.backend.post("service", data)

        # add service http
        data = json.loads(open('cfg/service_srv001_http.json').read())
        data['host'] = cls.data_host['_id']
        data['check_command'] = data_cmd_http['_id']
        data['_realm'] = cls.realm_all
        data['users'] = [data_user_jeronimo['_id']]
        data['usergroups'] = [data_usergroup['_id']]
        cls.data_srv_http = cls.backend.post("service", data)

        # Add some realms
        data = {
            'name': 'All-A',
            '_parent': cls.realm_all
        }
        realm_a = cls.backend.post("realm", data)
        data = {
            'name': 'All-B',
            '_parent': cls.realm_all
        }
        cls.backend.post("realm", data)
        data = {
            'name': 'All-A-1',
            '_parent': realm_a['_id']
        }
        cls.backend.post("realm", data)

    @classmethod
    def tearDownClass(cls):
        cls.p.kill()

    def setUp(self):
        self.maxDiff = None

        # Start arbiter backend module
        modconf = Module()
        modconf.module_alias = "backend_arbiter"
        modconf.username = "admin"
        modconf.password = "admin"
        modconf.api_url = 'http://127.0.0.1:5000'
        self.arbmodule = AlignakBackendArbiter(modconf)
        self.objects = self.arbmodule.get_objects()

        # Start broker module
        modconf = Module()
        modconf.module_alias = "backend_broker"
        modconf.username = "admin"
        modconf.password = "admin"
        modconf.api_url = 'http://127.0.0.1:5000'
        self.brokmodule = AlignakBackendBroker(modconf)

        # Set up the broker module
        self.brokmodule.get_refs()

    def test_00_refused_program_status_brok(self):
        """Test with a bad formatted brok for the program status

        :return: None
        """
        # Get alignak endpoint resources before the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        for alignak_cfg in all_alignak['_items']:
            print(("Alignak cfg: %s" % alignak_cfg))
        # No alignak configuration resource
        self.assertEqual(0, len(all_alignak['_items']))

        # Get a BAD program status brok
        brok_data = {
            # Some general information

            ### Missing alignak_name property !
            # u'alignak_name': u'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()

        # Send program status brok
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # Still no alignak configuration resource
        self.assertEqual(0, len(all_alignak['_items']))

        # Get a GOOD program status brok
        brok_data = {
            # Some general information

            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()

        # The module has no default realm ... this should never happen !
        self.brokmodule.default_realm = None

        # Send program status brok
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # Still no alignak configuration resource
        self.assertEqual(0, len(all_alignak['_items']))

    def test_01_program_status_brok(self):
        """Test with a brok for the program status update

        :return: None
        """
        # Get alignak endpoint resources before the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        for alignak_cfg in all_alignak['_items']:
            print(("Alignak cfg: %s" % alignak_cfg))
        # No alignak configuration resource
        self.assertEqual(0, len(all_alignak['_items']))

        # Get a program status brok
        brok_data = {
            # Some general information
            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()

        # As default, we do not manage this brok !
        assert self.brokmodule.manage_update_program_status is False

        # Send program status brok
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # Still no alignak configuration resource
        self.assertEqual(0, len(all_alignak['_items']))

        # -------
        # Now we manage this brok !
        self.brokmodule.manage_update_program_status = True

        # Send program status brok
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # Now we have one resource
        self.assertEqual(1, len(all_alignak['_items']))

        alignak = all_alignak['_items'][0]
        # Remove backend Eve fields and store creation and update timestamp
        _created = alignak.pop('_created')
        _updated = alignak.pop('_updated')
        alignak.pop('_id')
        alignak.pop('_links')
        alignak.pop('_etag')
        alignak.pop('schema_version')
        # TODO need add this new fields in alignak brok creation
        for field_name in ['use_timezone',
                           'illegal_macro_output_chars', 'illegal_object_name_chars',
                           'cleaning_queues_interval', 'max_plugins_output_length',
                           'enable_environment_macros', 'log_initial_states', 'log_active_checks',
                           'log_host_retries', 'log_service_retries', 'log_passive_checks',
                           'log_notifications', 'log_event_handlers', 'log_external_commands',
                           'log_flappings', 'log_snapshots', 'enable_notifications',
                           'notification_timeout', 'timeout_exit_status', 'execute_host_checks',
                           'max_host_check_spread', 'host_check_timeout',
                           'check_for_orphaned_hosts', 'execute_service_checks',
                           'max_service_check_spread', 'service_check_timeout',
                           'check_for_orphaned_services', 'flap_history', 'low_host_flap_threshold',
                           'high_host_flap_threshold', 'low_service_flap_threshold',
                           'high_service_flap_threshold', 'event_handler_timeout',
                           'no_event_handlers_during_downtimes', 'host_perfdata_command',
                           'service_perfdata_command', 'accept_passive_host_checks',
                           'host_freshness_check_interval', 'accept_passive_service_checks',
                           'service_freshness_check_interval', 'additional_freshness_latency']:
            alignak.pop(field_name)

        expected = brok_data.copy()
        expected['name'] = expected.pop('alignak_name')
        # Some fields are valued as default by the backend
        expected['_sub_realm'] = True
        expected['alias'] = expected['name']
        expected['notes'] = ''
        expected['notes_url'] = ''
        expected['_realm'] = self.realm_all
        expected['global_host_event_handler'] = str(expected['global_host_event_handler'])
        expected['global_service_event_handler'] = 'None'
        self.assertEqual(expected, alignak)

        # --- 1
        time.sleep(1)
        # Re-send the same brok
        brok_data = {
            # Some general information
            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # We still have one resource
        self.assertEqual(1, len(all_alignak['_items']))

        alignak = all_alignak['_items'][0]
        # Remove backend Eve fields
        # Creation and update timestamps did not change because there was no backend update
        assert _created == alignak.pop('_created')
        assert _updated == alignak.pop('_updated')
        alignak.pop('_id')
        alignak.pop('_links')
        alignak.pop('_etag')
        alignak.pop('schema_version')
        # TODO need add this new fields in alignak brok creation
        for field_name in ['use_timezone',
                           'illegal_macro_output_chars', 'illegal_object_name_chars',
                           'cleaning_queues_interval', 'max_plugins_output_length',
                           'enable_environment_macros', 'log_initial_states', 'log_active_checks',
                           'log_host_retries', 'log_service_retries', 'log_passive_checks',
                           'log_notifications', 'log_event_handlers', 'log_external_commands',
                           'log_flappings', 'log_snapshots', 'enable_notifications',
                           'notification_timeout', 'timeout_exit_status', 'execute_host_checks',
                           'max_host_check_spread', 'host_check_timeout',
                           'check_for_orphaned_hosts', 'execute_service_checks',
                           'max_service_check_spread', 'service_check_timeout',
                           'check_for_orphaned_services', 'flap_history', 'low_host_flap_threshold',
                           'high_host_flap_threshold', 'low_service_flap_threshold',
                           'high_service_flap_threshold', 'event_handler_timeout',
                           'no_event_handlers_during_downtimes', 'host_perfdata_command',
                           'service_perfdata_command', 'accept_passive_host_checks',
                           'host_freshness_check_interval', 'accept_passive_service_checks',
                           'service_freshness_check_interval', 'additional_freshness_latency']:
            alignak.pop(field_name)

        expected = brok_data.copy()
        expected['name'] = expected.pop('alignak_name')
        # Some fields are valued as default by the backend
        expected['_sub_realm'] = True
        expected['alias'] = expected['name']
        expected['notes'] = ''
        expected['notes_url'] = ''
        expected['_realm'] = self.realm_all
        expected['global_host_event_handler'] = str(expected['global_host_event_handler'])
        expected['global_service_event_handler'] = 'None'
        self.assertEqual(expected, alignak)

        # --- 2
        time.sleep(1)
        # Update the program status
        brok_data = {
            # Some general information
            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok_data['flap_detection_enabled'] = False
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()
        # Send program status brok
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # We still have one resource
        self.assertEqual(1, len(all_alignak['_items']))

        alignak = all_alignak['_items'][0]
        # Remove backend Eve fields
        # Creation timestamp did not change
        assert _created == alignak['_created']
        _created = alignak.pop('_created')
        # But update timestamp changed !
        assert _updated != alignak['_updated']
        _updated = alignak.pop('_updated')
        alignak.pop('_id')
        alignak.pop('_links')
        alignak.pop('_etag')
        alignak.pop('schema_version')
        # TODO need add this new fields in alignak brok creation
        for field_name in ['use_timezone',
                           'illegal_macro_output_chars', 'illegal_object_name_chars',
                           'cleaning_queues_interval', 'max_plugins_output_length',
                           'enable_environment_macros', 'log_initial_states', 'log_active_checks',
                           'log_host_retries', 'log_service_retries', 'log_passive_checks',
                           'log_notifications', 'log_event_handlers', 'log_external_commands',
                           'log_flappings', 'log_snapshots', 'enable_notifications',
                           'notification_timeout', 'timeout_exit_status', 'execute_host_checks',
                           'max_host_check_spread', 'host_check_timeout',
                           'check_for_orphaned_hosts', 'execute_service_checks',
                           'max_service_check_spread', 'service_check_timeout',
                           'check_for_orphaned_services', 'flap_history', 'low_host_flap_threshold',
                           'high_host_flap_threshold', 'low_service_flap_threshold',
                           'high_service_flap_threshold', 'event_handler_timeout',
                           'no_event_handlers_during_downtimes', 'host_perfdata_command',
                           'service_perfdata_command', 'accept_passive_host_checks',
                           'host_freshness_check_interval', 'accept_passive_service_checks',
                           'service_freshness_check_interval', 'additional_freshness_latency']:
            alignak.pop(field_name)

        expected = brok_data.copy()
        expected['name'] = expected.pop('alignak_name')
        # Some fields are valued as default by the backend
        expected['_sub_realm'] = True
        expected['alias'] = expected['name']
        expected['notes'] = ''
        expected['notes_url'] = ''
        expected['_realm'] = self.realm_all
        expected['global_host_event_handler'] = str(expected['global_host_event_handler'])
        expected['global_service_event_handler'] = 'None'
        self.assertEqual(expected, alignak)

        # --- 3
        time.sleep(1)
        # Re-send the same brok
        brok_data = {
            # Some general information
            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok_data['flap_detection_enabled'] = False
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # We still have one resource
        self.assertEqual(1, len(all_alignak['_items']))

        alignak = all_alignak['_items'][0]
        # Remove backend Eve fields
        # Creation timestamp do not change
        assert _created == alignak['_created']
        _created = alignak.pop('_created')
        # And update timestamp do not change!
        assert _updated == alignak['_updated']
        _updated = alignak.pop('_updated')
        alignak.pop('_id')
        alignak.pop('_links')
        alignak.pop('_etag')
        alignak.pop('schema_version')
        # TODO need add this new fields in alignak brok creation
        for field_name in ['use_timezone',
                           'illegal_macro_output_chars', 'illegal_object_name_chars',
                           'cleaning_queues_interval', 'max_plugins_output_length',
                           'enable_environment_macros', 'log_initial_states', 'log_active_checks',
                           'log_host_retries', 'log_service_retries', 'log_passive_checks',
                           'log_notifications', 'log_event_handlers', 'log_external_commands',
                           'log_flappings', 'log_snapshots', 'enable_notifications',
                           'notification_timeout', 'timeout_exit_status', 'execute_host_checks',
                           'max_host_check_spread', 'host_check_timeout',
                           'check_for_orphaned_hosts', 'execute_service_checks',
                           'max_service_check_spread', 'service_check_timeout',
                           'check_for_orphaned_services', 'flap_history', 'low_host_flap_threshold',
                           'high_host_flap_threshold', 'low_service_flap_threshold',
                           'high_service_flap_threshold', 'event_handler_timeout',
                           'no_event_handlers_during_downtimes', 'host_perfdata_command',
                           'service_perfdata_command', 'accept_passive_host_checks',
                           'host_freshness_check_interval', 'accept_passive_service_checks',
                           'service_freshness_check_interval', 'additional_freshness_latency']:
            alignak.pop(field_name)

        expected = brok_data.copy()
        expected['name'] = expected.pop('alignak_name')
        # Some fields are valued as default by the backend
        expected['_sub_realm'] = True
        expected['alias'] = expected['name']
        expected['notes'] = ''
        expected['notes_url'] = ''
        expected['_realm'] = self.realm_all
        expected['global_host_event_handler'] = str(expected['global_host_event_handler'])
        expected['global_service_event_handler'] = 'None'
        self.assertEqual(expected, alignak)

        # --- 4
        time.sleep(1)
        # Update only the running properties
        brok_data = {
            # Some general information
            'alignak_name': 'my_alignak',
            'instance_id': '176064a1b30741d39452415097807ab0',
            'instance_name': 'scheduler-master',

            # Some running information
            'program_start': 1493969754,
            'daemon_mode': 1,
            'pid': 68989,
            'last_alive': 1493970641,
            'last_command_check': 1493970641,
            'last_log_rotation': 1493970641,
            'is_running': 1,

            # Some configuration parameters
            'process_performance_data': True,
            'passive_service_checks_enabled': True,
            'event_handlers_enabled': True,
            'command_file': '',
            'global_host_event_handler': None,
            'interval_length': 60,
            'modified_host_attributes': 0,
            'check_external_commands': True,
            'modified_service_attributes': 0,
            'passive_host_checks_enabled': True,
            'global_service_event_handler': 'None',
            'notifications_enabled': True,
            'check_service_freshness': True,
            'check_host_freshness': True,
            'flap_detection_enabled': True,
            'active_service_checks_enabled': True,
            'active_host_checks_enabled': True
        }
        brok_data['flap_detection_enabled'] = False
        brok_data['last_alive'] = 123456789
        brok_data['last_command_check'] = 123456789
        brok_data['last_log_rotation'] = 123456789
        brok = Brok({'type': 'update_program_status', 'data': brok_data})
        brok.prepare()
        self.brokmodule.manage_brok(brok)

        # Get alignak endpoint resources after the brok
        name = 'my_alignak'
        params = {'sort': '_id', 'where': '{"name": "%s"}' % name}
        all_alignak = self.backend.get_all('alignak', params)
        # We still have one resource
        self.assertEqual(1, len(all_alignak['_items']))

        alignak = all_alignak['_items'][0]
        # Remove backend Eve fields
        # Creation timestamp do not change
        assert _created == alignak['_created']
        _created = alignak.pop('_created')
        # And update timestamp do not change!
        assert _updated == alignak['_updated']
        _updated = alignak.pop('_updated')
        alignak.pop('_id')
        alignak.pop('_links')
        alignak.pop('_etag')
        alignak.pop('schema_version')
        # TODO need add this new fields in alignak brok creation
        for field_name in ['use_timezone',
                           'illegal_macro_output_chars', 'illegal_object_name_chars',
                           'cleaning_queues_interval', 'max_plugins_output_length',
                           'enable_environment_macros', 'log_initial_states', 'log_active_checks',
                           'log_host_retries', 'log_service_retries', 'log_passive_checks',
                           'log_notifications', 'log_event_handlers', 'log_external_commands',
                           'log_flappings', 'log_snapshots', 'enable_notifications',
                           'notification_timeout', 'timeout_exit_status', 'execute_host_checks',
                           'max_host_check_spread', 'host_check_timeout',
                           'check_for_orphaned_hosts', 'execute_service_checks',
                           'max_service_check_spread', 'service_check_timeout',
                           'check_for_orphaned_services', 'flap_history', 'low_host_flap_threshold',
                           'high_host_flap_threshold', 'low_service_flap_threshold',
                           'high_service_flap_threshold', 'event_handler_timeout',
                           'no_event_handlers_during_downtimes', 'host_perfdata_command',
                           'service_perfdata_command', 'accept_passive_host_checks',
                           'host_freshness_check_interval', 'accept_passive_service_checks',
                           'service_freshness_check_interval', 'additional_freshness_latency']:
            alignak.pop(field_name)

        expected = brok_data.copy()
        expected['name'] = expected.pop('alignak_name')
        # Some fields are valued as default by the backend
        expected['_sub_realm'] = True
        expected['alias'] = expected['name']
        expected['notes'] = ''
        expected['notes_url'] = ''
        expected['_realm'] = self.realm_all
        expected['global_host_event_handler'] = str(expected['global_host_event_handler'])
        expected['global_service_event_handler'] = 'None'
        self.assertEqual(expected, alignak)

    def check_host_brok(self, prop, value):
        # Get an host and its full status brok
        self.objects = self.arbmodule.get_objects()
        my_host = None
        for host in self.objects['hosts']:
            if host['host_name'] == 'srv001':
                my_host = Host(host)
        # Get host status brok
        data = {'uuid': '0123456789'}
        my_host.fill_data_brok_from(data, 'full_status')

        # Update brok data
        if prop not in data:
            print(("Host property '%s' does not exit!" % prop))
            return False
        data[prop] = value
        brok = Brok({'type': 'update_host_status', 'data': data})
        brok.prepare()
        print(("Brok: %s" % brok))

        # Send host status brok
        self.brokmodule.manage_brok(brok)

        # Get host data like an arbiter to check modification
        self.objects = self.arbmodule.get_objects()
        my_changed_host = None
        for host in self.objects['hosts']:
            if host['host_name'] == 'srv001':
                my_changed_host = Host(host)
        # Get host status brok
        data = {'uuid': '0123456789'}
        my_changed_host.fill_data_brok_from(data, 'full_status')
        brok_bis = Brok({'type': 'update_host_status', 'data': data})
        brok_bis.prepare()
        print(("Brok: %s" % brok_bis))

        # Broks data are equal, nothing changed
        self.assertEqual(brok.data, brok_bis.data)

        return True

    def test_10_brok_host_update_boolean(self):
        """Test with a brok for an host update - boolean properties

        :return: None
        """
        self.maxDiff = None

        for prop in ['event_handler_enabled', 'active_checks_enabled', 'passive_checks_enabled',
                     'flap_detection_enabled', 'check_freshness', 'notifications_enabled']:
            self.assertTrue(self.check_host_brok(prop, True))
            self.assertTrue(self.check_host_brok(prop, False))

        self.assertTrue(self.check_host_brok('customs', {'_A': 'a', '_B': '1'}))
        self.assertTrue(self.check_host_brok('check_interval', 1234))
        self.assertTrue(self.check_host_brok('retry_interval', 1234))
        self.assertTrue(self.check_host_brok('first_notification_delay', 1234))

    def check_service_brok(self, prop, value):
        # Get an service and its full status brok
        self.objects = self.arbmodule.get_objects()
        my_service = None
        for service in self.objects['services']:
            if service['host_name'] == 'srv001' and service['service_description'] == 'ping':
                my_service = Service(service)
        # Get service status brok
        data = {'uuid': '0123456789'}
        my_service.fill_data_brok_from(data, 'full_status')

        # Update brok data
        if prop not in data:
            print(("service property '%s' does not exit!" % prop))
            return False
        data[prop] = value
        brok = Brok({'type': 'update_service_status', 'data': data})
        brok.prepare()
        print(("Before: %s" % brok))

        # Send service status brok
        self.brokmodule.manage_brok(brok)

        # Get service data like an arbiter to check modification
        self.objects = self.arbmodule.get_objects()
        my_changed_service = None
        for service in self.objects['services']:
            if service['host_name'] == 'srv001' and service['service_description'] == 'ping':
                my_changed_service = Service(service)
        # Get service status brok
        data = {'uuid': '0123456789'}
        my_changed_service.fill_data_brok_from(data, 'full_status')
        brok_bis = Brok({'type': 'update_service_status', 'data': data})
        brok_bis.prepare()
        print(("After: %s" % brok_bis))

        # Broks data are equal, nothing changed
        self.assertEqual(brok.data, brok_bis.data)

        return True

    def test_11_brok_service_update_boolean(self):
        """Test with a brok for an service update - boolean properties

        :return: None
        """
        self.maxDiff = None

        for prop in ['event_handler_enabled', 'active_checks_enabled', 'passive_checks_enabled',
                     'flap_detection_enabled', 'check_freshness', 'notifications_enabled']:
            # Update several times...
            self.assertTrue(self.check_service_brok(prop, True))
            self.assertTrue(self.check_service_brok(prop, False))
            self.assertTrue(self.check_service_brok(prop, True))
            self.assertTrue(self.check_service_brok(prop, False))

        self.assertTrue(self.check_service_brok('customs', {'_A': 'a', '_B': '1'}))
        self.assertTrue(self.check_service_brok('check_interval', 1234))
        self.assertTrue(self.check_service_brok('retry_interval', 1234))
        self.assertTrue(self.check_service_brok('first_notification_delay', 1234))

    def check_user_brok(self, prop, value):
        # Get a contact and its full status brok
        self.objects = self.arbmodule.get_objects()
        my_user = None
        for user in self.objects['contacts']:
            if user['contact_name'] == 'jeronimo':
                my_user = Contact(user)
        # Get user status brok
        data = {'uuid': '0123456789'}
        my_user.fill_data_brok_from(data, 'full_status')

        # Update brok data
        if prop not in data:
            return False
        data[prop] = value
        brok = Brok({'type': 'update_contact_status', 'data': data})
        brok.prepare()
        print(("Brok: %s" % brok))

        # Send user status brok
        self.brokmodule.manage_brok(brok)

        # Get user data like an arbiter to check modification
        self.objects = self.arbmodule.get_objects()
        my_changed_user = None
        for user in self.objects['contacts']:
            if user['contact_name'] == 'jeronimo':
                my_changed_user = Contact(user)
        # Get user status brok
        data = {'uuid': '0123456789'}
        my_changed_user.fill_data_brok_from(data, 'full_status')
        brok_bis = Brok({'type': 'update_contact_status', 'data': data})
        brok_bis.prepare()
        print(("Brok: %s" % brok_bis))

        # Broks data are equal, nothing changed
        self.assertEqual(brok.data, brok_bis.data)
        return True

    def test_12_brok_user_update_boolean(self):
        """Test with a brok for a user update - boolean properties

        :return: None
        """
        for prop in ['host_notifications_enabled', 'service_notifications_enabled']:
            self.assertTrue(self.check_user_brok(prop, True))
            self.assertTrue(self.check_user_brok(prop, False))

        self.assertTrue(self.check_user_brok('customs', {'_A': 'a', '_B': '1'}))
