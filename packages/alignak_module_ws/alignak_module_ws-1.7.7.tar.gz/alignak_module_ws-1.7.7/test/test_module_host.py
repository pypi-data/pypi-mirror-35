#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2016: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
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
#
"""
Test the module
"""

import os
import time
import json

import pytest

from freezegun import freeze_time

import shlex
import subprocess

import requests

from .alignak_test import AlignakTest
from alignak.modulesmanager import ModulesManager
from alignak.objects.module import Module
from alignak.daemons.receiverdaemon import Receiver

# Set environment variable to ask code Coverage collection
os.environ['COVERAGE_PROCESS_START'] = '.coveragerc'

import alignak_module_ws


class TestModuleWsHost(AlignakTest):
    """This class contains the tests for the module"""

    @classmethod
    def setUpClass(cls):

        # Simulate an Alignak receiver daemon
        cls.ws_endpoint = 'http://127.0.0.1:7773/ws'
        import cherrypy
        class ReceiverItf(object):
            @cherrypy.expose
            def index(self):
                return "I am the Receiver daemon!"
        from alignak.http.daemon import HTTPDaemon as AlignakDaemon
        http_daemon1 = AlignakDaemon('0.0.0.0', 7773, ReceiverItf(),
                                     False, None, None, None, None, 10, '/tmp/alignak-cherrypy.log')
        def run_http_server():
            http_daemon1.run()
        import threading
        cls.http_thread1 = threading.Thread(target=run_http_server, name='http_server_receiver')
        cls.http_thread1.daemon = True
        cls.http_thread1.start()
        print("Thread started")

        # Set test mode for alignak backend
        os.environ['TEST_ALIGNAK_BACKEND'] = '1'
        os.environ['ALIGNAK_BACKEND_MONGO_DBNAME'] = 'alignak-module-ws-host'
        os.environ['ALIGNAK_BACKEND_CONFIGURATION_FILE'] = './cfg/backend/settings.json'

        # Delete used mongo DBs
        print ("Deleting Alignak backend DB...")
        exit_code = subprocess.call(
            shlex.split(
                'mongo %s --eval "db.dropDatabase()"' % os.environ['ALIGNAK_BACKEND_MONGO_DBNAME'])
        )
        assert exit_code == 0

        if os.path.exists('/tmp/alignak-backend_%s.log' % os.environ['ALIGNAK_BACKEND_MONGO_DBNAME']):
            os.remove('/tmp/alignak-backend_%s.log' % os.environ['ALIGNAK_BACKEND_MONGO_DBNAME'])

        fnull = open(os.devnull, 'w')
        cls.p = subprocess.Popen(['uwsgi', '--plugin', 'python', '-w', 'alignakbackend:app',
                                  '--socket', '0.0.0.0:5000',
                                  '--protocol=http', '--enable-threads', '--pidfile',
                                  '/tmp/uwsgi.pid'],
                                 stdout=fnull, stderr=fnull)
        time.sleep(3)

        test_dir = os.path.dirname(os.path.realpath(__file__))
        print(("Current test directory: %s" % test_dir))

        print(("Feeding Alignak backend... %s" % test_dir))
        exit_code = subprocess.call(
            shlex.split('alignak-backend-import --delete %s/cfg/cfg_default.cfg' % test_dir),
            stdout=fnull, stderr=fnull
        )
        assert exit_code == 0
        print("Fed")

        cls.endpoint = 'http://127.0.0.1:5000'

        # Backend authentication
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        # Get admin user token (force regenerate)
        response = requests.post(cls.endpoint + '/login', json=params, headers=headers)
        resp = response.json()
        cls.token = resp['token']
        cls.auth = requests.auth.HTTPBasicAuth(cls.token, '')

        # Get admin user
        response = requests.get(cls.endpoint + '/user', auth=cls.auth)
        resp = response.json()
        cls.user_admin = resp['_items'][0]

        # Get realms
        response = requests.get(cls.endpoint + '/realm', auth=cls.auth)
        resp = response.json()
        cls.realmAll_id = resp['_items'][0]['_id']

        # Add a user
        data = {'name': 'test', 'password': 'test', 'back_role_super_admin': False,
                'host_notification_period': cls.user_admin['host_notification_period'],
                'service_notification_period': cls.user_admin['service_notification_period'],
                '_realm': cls.realmAll_id}
        response = requests.post(cls.endpoint + '/user', json=data, headers=headers,
                                 auth=cls.auth)
        resp = response.json()
        print(("Created a new user: %s" % resp))

        # Get new user restrict role
        params = {'where': json.dumps({'user': resp['_id']})}
        response = requests.get(cls.endpoint + '/userrestrictrole', params=params, auth=cls.auth)
        resp = response.json()

        # Update user's rights - set full CRUD rights
        headers = {'Content-Type': 'application/json', 'If-Match': resp['_items'][0]['_etag']}
        data = {'crud': ['create', 'read', 'update', 'delete', 'custom']}
        resp = requests.patch(cls.endpoint + '/userrestrictrole/' + resp['_items'][0]['_id'],
                              json=data, headers=headers, auth=cls.auth)
        resp = resp.json()
        assert resp['_status'] == 'OK'

        cls.modulemanager = None

        cls.maxDiff = None

    @classmethod
    def tearDownClass(cls):
        cls.p.kill()

    def setUp(self):
        super(TestModuleWsHost, self).setUp()

    def tearDown(self):
        super(TestModuleWsHost, self).tearDown()
        if self.modulemanager:
            time.sleep(1)
            self.modulemanager.stop_all()

    def test_module_zzz_host(self):
        """Test the module /host API
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Give result data
            'give_result': '1',
            # Give some feedback about host and services
            'give_feedback': '2',
            'feedback_host': 'alias,notes,location,active_checks_enabled,max_check_attempts,check_interval,retry_interval,passive_checks_enabled,check_freshness,freshness_state,freshness_threshold,_overall_state_id',
            'feedback_service': 'alias,notes,active_checks_enabled,max_check_attempts,check_interval,retry_interval,passive_checks_enabled,check_freshness,freshness_state,freshness_threshold,_overall_state_id',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # POST request on /host - forbidden to POST
        response = session.post(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 415)

        # PUT request on /host - forbidden to PUT
        response = session.put(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 415)

        # Allowed GET request on /host - forbidden to GET
        response = session.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_result'], '')
        self.assertEqual(result['_issues'], ['Missing targeted element.'])

        self.show_logs()

        # You must have parameters when PATCHing on /host
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_error'], 'You must send parameters on this endpoint.')

        # When host does not exist...
        data = {
            "fake": ""
        }
        response = session.patch(self.ws_endpoint + '/host/test_host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['test_host is alive :)'],
                                  '_issues': ["Requested host 'test_host' does not exist. Note that host creation is not allowed."]})

        # Host name may be the last part of the URI
        data = {
            "fake": ""
        }
        response = session.patch(self.ws_endpoint + '/host/test_host_0', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)'],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Host name may be in the POSTed data
        data = {
            "name": "test_host_0",
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)'],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Host name in the POSTed data takes precedence over URI
        data = {
            "name": "test_host_0",
        }
        response = session.patch(self.ws_endpoint + '/host/other_host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)'],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Host name must be somewhere !
        headers = {'Content-Type': 'application/json'}
        data = {
            "fake": "test_host",
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_issues'], ['Missing targeted element.'])

        # Update host livestate (heartbeat / host is alive): empty livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "livestate": "",
            "name": "test_host_0",
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)'],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Update host livestate (heartbeat / host is alive): missing state in the livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['test_host_0 is alive :)'],
                                  '_issues': ['Missing state in the livestate.']})

        # Update host livestate (heartbeat / host is alive): livestate must have an accepted state
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 0)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['test_host_0 is alive :)'],
                                  '_issues': ["Host state must be UP, DOWN or UNREACHABLE, "
                                               "and not ''."]})

        # Update host livestate (heartbeat / host is alive): livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "UP",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 1)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "PROCESS_HOST_CHECK_RESULT;test_host_0;0;"
                         "Output...|'counter'=1\nLong output...",
                         # u"Host 'test_host_0' updated."
                         ],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Update host livestate (heartbeat / host is alive): livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "unreachable",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 2)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "PROCESS_HOST_CHECK_RESULT;test_host_0;2;"
                         "Output...|'counter'=1\nLong output...",
                         # u"Host 'test_host_0' updated."
                         ],
            '_feedback': {
                'name': 'test_host_0',
                '_overall_state_id': 3,
                'active_checks_enabled': True,
                'alias': 'up_0',
                'check_freshness': False,
                'check_interval': 1,
                'freshness_state': 'x',
                'freshness_threshold': 60,
                'location': {'coordinates': [48.858293, 2.294601],
                              'type': 'Point'},
                'max_check_attempts': 3,
                'notes': '',
                'passive_checks_enabled': True,
                'retry_interval': 1
            }
        })

        # Update host services livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "up",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1"
            },
            "services": [
                {
                    "name": "test_ok_0",
                    "livestate": {
                        "state": "ok",
                        "output": "Output 0",
                        "long_output": "Long output 0",
                        "perf_data": "'counter'=0"
                    }
                },
                {
                    "name": "test_ok_1",
                    "livestate": {
                        "state": "warning",
                        "output": "Output 1",
                        "long_output": "Long output 1",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output 2",
                        "long_output": "Long output 2",
                        "perf_data": "'counter'=2"
                    }
                },
            ]
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                "PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output...",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output 0|'counter'=0\nLong output 0",
                # u"Service 'test_host_0/test_ok_0' updated",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output 1|'counter'=1\nLong output 1",
                # u"Service 'test_host_0/test_ok_1' updated",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output 2|'counter'=2\nLong output 2",
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated.",
            ],
            '_feedback': {
                'active_checks_enabled': True, '_overall_state_id': 3, 'freshness_state': 'x',
                'notes': '', 'retry_interval': 1, 'name': 'test_host_0', 'alias': 'up_0',
                'freshness_threshold': 60,
                'location': {'type': 'Point', 'coordinates': [48.858293, 2.294601]},
                'check_interval': 1,
                'max_check_attempts': 3, 'check_freshness': False,
                'passive_checks_enabled': True,

                'services': [
                    {
                        'name': 'test_ok_0', 'alias': 'test_host_0 test_ok_0',
                        'freshness_state': 'x', 'notes': 'just a notes string',
                        'retry_interval': 1, '_overall_state_id': 5,
                        'freshness_threshold': 60, 'check_interval': 1,
                        'max_check_attempts': 2,
                        'active_checks_enabled': False,
                        'check_freshness': False,
                        'passive_checks_enabled': False,
                    },
                    {
                        'name': 'test_ok_1', 'alias': 'test_host_0 test_ok_1',
                        'freshness_state': 'x', 'notes': 'just a notes string',
                        'retry_interval': 1, '_overall_state_id': 3,
                        'freshness_threshold': 60, 'check_interval': 1,
                        'max_check_attempts': 2,
                        'active_checks_enabled': True,
                        'check_freshness': False,
                        'passive_checks_enabled': True,
                    },
                    {
                        'name': 'test_ok_2', 'alias': 'test_host_0 test_ok_2',
                        'freshness_state': 'x', 'notes': 'just a notes string',
                        'retry_interval': 1, '_overall_state_id': 3,
                        'freshness_threshold': 60, 'check_interval': 1,
                        'max_check_attempts': 2,
                        'active_checks_enabled': False,
                        'check_freshness': False,
                        'passive_checks_enabled': True,
                    }
                ]
            }
        })
        # 4 more commands at once
        self.assertEqual(my_module.received_commands, 6)

        # Logout
        print("Logout...")
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        time.sleep(1.0)
        self.modulemanager.stop_all()

    def test_module_zzz_simulate_host(self):
        """Simulate an host on the /host API - no feedback
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Give result data
            'give_result': '1',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # No feedback
            'give_feedback': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # Host name
        host_name = 'test_host_0'

        # Update host services livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": host_name,
            "livestate": {
                "state": "up",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1"
            },
            "services": [
                {
                    "name": "test_ok_0",
                    "livestate": {
                        "state": "ok",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_1",
                    "livestate": {
                        "state": "warning",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
            ],
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK', '_result': [
                'test_host_0 is alive :)',
                "PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output...",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output...",
                # u"Service 'test_host_0/test_ok_0' updated",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output...|'counter'=1\nLong output...",
                # u"Service 'test_host_0/test_ok_1' updated",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output...|'counter'=1\nLong output...",
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated."
            ]
        })

        # Update host services livestate - several checks in the livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": host_name,
            "livestate": [
                {
                    "timestamp": 123456789,
                    "state": "up",
                    "output": "Output...",
                    "long_output": "Long output...",
                    "perf_data": "'counter'=1"
                },
                {
                    "timestamp": 123456789 + 3600,
                    "state": "up",
                    "output": "Output...",
                    "long_output": "Long output...",
                    "perf_data": "'counter'=1"
                }
            ],
            "services": [
                {
                    "name": "test_ok_0",
                    # An array with one item
                    "livestate": [
                        {
                            "timestamp": 123456789,
                            "state": "ok",
                            "output": "Output...",
                            "long_output": "Long output...",
                            "perf_data": "'counter'=1"
                        }
                    ]
                },
                {
                    "name": "test_ok_1",
                    # An array with one item
                    "livestate": [
                        {
                            "timestamp": 123456789,
                            "state": "warning",
                            "output": "Output...",
                            "long_output": "Long output...",
                            "perf_data": "'counter'=1"
                        },
                        {
                            "timestamp": 123456789 + 3600,
                            "state": "ok",
                            "output": "Output...",
                            "long_output": "Long output...",
                            "perf_data": "'counter'=2"
                        }
                    ]
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
            ],
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK', '_result': [
                'test_host_0 is alive :)',
                "[123456789] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output...",
                "[123460389] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output...",
                # u"Host 'test_host_0' updated.",
                # u"Host 'test_host_0' updated.",
                "[123456789] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output...",
                # u"Service 'test_host_0/test_ok_0' updated",
                "[123456789] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output...|'counter'=1\nLong output...",
                "[123460389] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;0;Output...|'counter'=2\nLong output...",
                # u"Service 'test_host_0/test_ok_1' updated",
                "PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output...|'counter'=1\nLong output...",
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated."
            ]
        })

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    @freeze_time("2017-06-01 18:30:00")
    def test_module_zzz_host_timestamp(self):
        """Test the module /host API
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Give result data
            'give_result': '1',
            # Timestamp
            'set_timestamp': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })
        print("Module...")

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)
        print("Daemon...")

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())
        time.sleep(1.0)
        print("My module PID: %s" % my_module.process.pid)

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()
        print("Login...")

        # You must have parameters when POSTing on /host
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_error'], 'You must send parameters on this endpoint.')

        # When host does not exist...
        headers = {'Content-Type': 'application/json'}
        data = {
            "fake": ""
        }
        response = session.patch(self.ws_endpoint + '/host/test_host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['test_host is alive :)'],
                                  '_issues': ["Requested host 'test_host' does not exist. "
                                               "Note that host creation is not allowed."]})

        # Host name may be the last part of the URI
        headers = {'Content-Type': 'application/json'}
        data = {
            "fake": ""
        }
        response = session.patch(self.ws_endpoint + '/host/test_host_0', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # Host name may be in the POSTed data
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # Host name in the POSTed data takes precedence over URI
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
        }
        response = session.patch(self.ws_endpoint + '/host/other_host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # Host name must be somewhere !
        headers = {'Content-Type': 'application/json'}
        data = {
            "fake": "test_host",
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_issues'], ['Missing targeted element.'])

        # Update host livestate (heartbeat / host is alive): empty livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "livestate": "",
            "name": "test_host_0",
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # Update host livestate (heartbeat / host is alive): missing state in the livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['test_host_0 is alive :)'],
            '_issues': ['Missing state in the livestate.']
        })

        # Update host livestate (heartbeat / host is alive): livestate must have an accepted state
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['test_host_0 is alive :)'],
            '_issues': ["Host state must be UP, DOWN or UNREACHABLE, and not ''."]})

        # Update host livestate (heartbeat / host is alive): livestate must have an accepted state
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "XxX",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['test_host_0 is alive :)'],
            '_issues': ["Host state must be UP, DOWN or UNREACHABLE, and not 'XXX'."]})

        # Update host livestate (heartbeat / host is alive): livestate, no timestamp
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "UP",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 1)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;"
                         "Output...|'counter'=1\nLong output..." % time.time(),
                         # u"Host 'test_host_0' updated."
            ]
        })

        # Update host livestate (heartbeat / host is alive): livestate, provided timestamp
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "timestamp": 123456789,
                "state": "UP",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        self.assertEqual(my_module.received_commands, 1)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 2)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output..." % 123456789,
                         # u"Host 'test_host_0' updated."
                        ]
        })

        # Update host livestate (heartbeat / host is alive): livestate may be a list
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": [
                {
                    "timestamp": 123456789,
                    "state": "UP",
                    "output": "Output...",
                    "long_output": "Long output...",
                    "perf_data": "'counter'=1",
                },
                {
                    "timestamp": 987654321,
                    "state": "UP",
                    "output": "Output...",
                    "long_output": "Long output...",
                    "perf_data": "'counter'=1",
                }
            ]
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 4)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;"
                         "Output...|'counter'=1\nLong output..." % 123456789,
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;"
                         "Output...|'counter'=1\nLong output..." % 987654321,
                         # u"Host 'test_host_0' updated."
                         ]
        })

        # Update host livestate (heartbeat / host is alive): livestate, invalid provided timestamp
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "timestamp": "ABC", # Invalid!
                "state": "UP",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 5)
        result = response.json()
        # A timestamp is set because the module is configured to set a timestamp,
        # even if the provided one is not valid!
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;"
                         "Output...|'counter'=1\nLong output..." % time.time(),
                         # u"Host 'test_host_0' updated."
                         ]
        })

        # Update host livestate (heartbeat / host is alive): livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "unreachable",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1",
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 6)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;2;"
                         "Output...|'counter'=1\nLong output..." % time.time(),
                         # u"Host 'test_host_0' updated."
                         ]
        })

        # Update host services livestate
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "up",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1"
            },
            "services": [
                {
                    "name": "test_ok_0",
                    "livestate": {
                        "state": "ok",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_1",
                    "livestate": {
                        "state": "warning",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
            ],
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        now = time.time()
        self.assertEqual(result, {
            '_status': 'OK', '_result': [
                'test_host_0 is alive :)',
                "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output..." % now,
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_0' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_1' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated."
            ]
        })
        self.assertEqual(my_module.received_commands, 10)

        # Update host services livestate - provided timestamp
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "up",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1"
            },
            "services": [
                {
                    "name": "test_ok_0",
                    "livestate": {
                        "timestamp": 123456789,
                        "state": "ok",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_1",
                    "livestate": {
                        "state": "warning",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
            ],
        }
        now = time.time()
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 14)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK', '_result': [
                'test_host_0 is alive :)',
                "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output..." % now,
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output..." % 123456789,
                # u"Service 'test_host_0/test_ok_0' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_1' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated."
            ]
        })

        # Update host services livestate - livestate may be a list
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "livestate": {
                "state": "up",
                "output": "Output...",
                "long_output": "Long output...",
                "perf_data": "'counter'=1"
            },
            "services": [
                {
                    "name": "test_ok_0",
                    "livestate": [
                        {
                            "timestamp": 123456789,
                            "state": "ok",
                            "output": "Output...",
                            "long_output": "Long output...",
                            "perf_data": "'counter'=1"
                        },
                        {
                            "timestamp": 987654321,
                            "state": "ok",
                            "output": "Output...",
                            "long_output": "Long output...",
                            "perf_data": "'counter'=1"
                        }
                    ]
                },
                {
                    "name": "test_ok_1",
                    "livestate": {
                        "state": "warning",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "test_ok_2",
                    "livestate": {
                        "state": "critical",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
            ],
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(my_module.received_commands, 19)
        result = response.json()
        now = time.time()
        self.assertEqual(result, {
            '_status': 'OK', '_result': [
                'test_host_0 is alive :)',
                "[%d] PROCESS_HOST_CHECK_RESULT;test_host_0;0;Output...|'counter'=1\nLong output..." % now,
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output..." % 123456789,
                # u"Service 'test_host_0/test_ok_0' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_0;0;Output...|'counter'=1\nLong output..." % 987654321,
                # u"Service 'test_host_0/test_ok_0' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_1;1;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_1' updated",
                "[%d] PROCESS_SERVICE_CHECK_RESULT;test_host_0;test_ok_2;2;Output...|'counter'=1\nLong output..." % now,
                # u"Service 'test_host_0/test_ok_2' updated",
                # u"Host 'test_host_0' updated."
            ]
        })

        # Logout
        print("Logout...")
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        time.sleep(1.0)
        # self.modulemanager.stop_all()

    def test_module_zzz_host_variables(self):
        """Test the module /host API * create/update custom variables
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # ---

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # You must have parameters when POSTing on /host
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_error'], 'You must send parameters on this endpoint.')

        # Update host variables - empty variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": "",
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)'],
        })

        # ----------
        # Host does not exist
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "unknown_host",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['unknown_host is alive :)'],
                                  '_issues': ["Requested host 'unknown_host' does not exist. "
                                               "Note that host creation is not allowed."]})


        # ----------
        # Create host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ["test_host_0 is alive :)",
                         "Host 'test_host_0' unchanged."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 5.0, '_TEST2': 1, '_TEST1': 'string'
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # ----------
        # Unchanged host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' unchanged."],
        })

        # Get host data to confirm there was not update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 5.0, '_TEST2': 1, '_TEST1': 'string'
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # ----------
        # Update host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string modified',
                'test2': 12,
                'test3': 15055.0,
                'test4': "new!"
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' updated."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 15055.0, '_TEST2': 12, '_TEST1': 'string modified', '_TEST4': 'new!'
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # ----------
        # Delete host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string modified',
                'test2': 12,
                'test3': 15055.0,
                'test4': "__delete__"
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ["test_host_0 is alive :)", "Host 'test_host_0' updated."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # todo: expected should be this:
        # currently it is not possible to update/delete a backend dict property!
        # expected = {
        #     u'_TEST3': 15055.0, u'_TEST2': 12, u'_TEST1': u'string modified'
        # }
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 15055.0, '_TEST2': 12, '_TEST1': 'string modified', '_TEST4': 'new!'
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_unknown_service(self):
        """Test the module /host API * unknown service
        give result, no feedback, do not ignore
        :return:
        """
        extra_conf = {
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0'
        }
        expected_result = {
            '_status': 'ERR',
            '_issues': [
                "Requested service 'test_host_0/unknown_service_0' does not exist. Note that service creation is not allowed.",
                "Requested service 'test_host_0/unknown_service_1' does not exist. Note that service creation is not allowed."
            ],
            '_result': ['test_host_0 is alive :)'],
        }
        self._manage_host_unknown_service(extra_conf=extra_conf, expected_result=expected_result)

    def test_module_zzz_host_unknown_service_2(self):
        """Test the module /host API * unknown service
        give result, give feedback, do not ignore
        :return:
        """
        extra_conf = {
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '1',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0'
        }
        expected_result = {
            '_status': 'ERR',
            '_feedback': {},
            '_issues': [
                "Requested service 'test_host_0/unknown_service_0' does not exist. Note that service creation is not allowed.",
                "Requested service 'test_host_0/unknown_service_1' does not exist. Note that service creation is not allowed."
            ],
            '_result': ['test_host_0 is alive :)'],
        }
        self._manage_host_unknown_service(extra_conf=extra_conf, expected_result=expected_result)

    def test_module_zzz_host_unknown_service_3(self):
        """Test the module /host API * unknown service
        give result, no feedback, ignore unknown host and service
        :return:
        """
        extra_conf = {
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '1',
            'ignore_unknown_service': '1'
        }
        expected_result = {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                "Requested service 'test_host_0/unknown_service_0' does not exist. Note that service creation is not allowed.",
                "Requested service 'test_host_0/unknown_service_1' does not exist. Note that service creation is not allowed."
            ]
        }
        self._manage_host_unknown_service(extra_conf=extra_conf, expected_result=expected_result)

    def _manage_host_unknown_service(self, extra_conf=None, expected_result=None):
        """Test the module /host API * unknown service and no creation allowed
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod_conf = {
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        }
        mod_conf.update(extra_conf)
        mod = Module(mod_conf)

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm tha the host still exists
        # ---
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # ---

        # Alignak WS connection
        # ---
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        session = requests.Session()
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()
        self.token = resp['_result'][0]
        self.auth_ws = requests.auth.HTTPBasicAuth(self.token, '')

        # Update host service - service does not exist
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "services": [
                {
                    "name": "unknown_service_0",
                    "livestate": {
                        "state": "OK",
                        "output": "Output...",
                        "long_output": "Long output...",
                        "perf_data": "'counter'=1"
                    }
                },
                {
                    "name": "unknown_service_1",
                    "livestate": {
                        "state": "OK",
                        "output": "Output..."
                    }
                }
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, expected_result)

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_variables_as_array(self):
        """Test the module /host API * create/update custom variables
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Give result data
            'give_result': '1',
            # No feedback
            'give_feedback': '0',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        print(("My host customs: %s" % test_host_0['customs']))
        # ---

        # Get services data to confirm update
        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': test_host_0['_id'],
                                                             'name': 'test_ok_0'})})
        resp = response.json()
        test_service_0 = resp['_items'][0]
        print(("My service customs: %s" % test_service_0['customs']))

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # ----------
        # New host variables as an array
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string modified',
                'test2': 12,
                'test3': 15055.0,
                'test4': "new!",
                'my_array': [
                    {
                        "id": "identifier", "name": "my name", "other": 1
                    },
                    {
                        "id": "identifier", "name": "my name", "other": 1
                    }
                ],
                'my_array_of_strings': [
                    "string1", "string2", "string3"
                ],
                'my_array_of_integers': [
                    1, 2, 3
                ],
                "List_Packages": [
                    {
                        "id": "adobereader"
                        , "version": "3.0.0"
                        , "service": "soft_adobereader"
                    }, {
                        "id": "cwrsync"
                        , "version": "3.1.2"
                        , "service": "soft_cwrsync"
                    }, {
                        "id": "HomeMaison"
                        , "version": "0.1.0"
                        , "service": "HomeMaison"
                    }, {
                        "id": "Inventory"
                        , "version": "4.0.4"
                        , "service": "soft_Inventory"
                    }
                ],
                'packages': [
                    {
                        "id": "identifier", "name": "Package 1", "other": 1
                    },
                    {
                        "id": "identifier", "name": "Package 2", "other": 1
                    }
                ]
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' updated."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 15055.0, '_TEST2': 12, '_TEST1': 'string modified', '_TEST4': 'new!',
            '_MY_ARRAY': [
                {'id': 'identifier', 'name': 'my name', 'other': 1},
                {'id': 'identifier', 'name': 'my name', 'other': 1}
            ],
            '_MY_ARRAY_OF_INTEGERS': [1, 2, 3],
            '_MY_ARRAY_OF_STRINGS': ['string1', 'string2', 'string3'],
            '_LIST_PACKAGES': [
                {'id': 'adobereader',
                 'service': 'soft_adobereader',
                 'version': '3.0.0'},
                {'id': 'cwrsync',
                 'service': 'soft_cwrsync',
                 'version': '3.1.2'},
                {'id': 'HomeMaison',
                 'service': 'HomeMaison',
                 'version': '0.1.0'},
                {'id': 'Inventory',
                 'service': 'soft_Inventory',
                 'version': '4.0.4'}
            ],
            '_PACKAGES': [
                {'id': 'identifier', 'name': 'Package 1', 'other': 1},
                {'id': 'identifier', 'name': 'Package 2', 'other': 1}
            ],
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # ----------
        # New host variables as an array - array order is not the same but not update!
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string modified',
                'test2': 12,
                'test3': 15055.0,
                'my_array': [
                    {
                        "id": "identifier", "name": "my name", "other": 1
                    },
                    {
                        "id": "identifier", "name": "my name", "other": 1
                    }
                ],
                'my_array_of_integers': [
                    1, 2, 3
                ],
                "List_Packages": [
                    {
                    "id": "adobereader"
                    , "version": "3.0.0"
                    , "service": "soft_adobereader"
                    }, {
                    "id": "cwrsync"
                    , "version": "3.1.2"
                    , "service": "soft_cwrsync"
                    }
                ],
                'packages': [
                    {
                        "id": "identifier", "name": "Package 1", "other": 1
                    },
                    {
                        "id": "identifier", "name": "Package 2", "other": 1
                    }
                ]
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' unchanged."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 15055.0, '_TEST2': 12, '_TEST1': 'string modified', '_TEST4': 'new!',
            '_MY_ARRAY': [
                {'id': 'identifier', 'name': 'my name', 'other': 1},
                {'id': 'identifier', 'name': 'my name', 'other': 1}
            ],
            '_MY_ARRAY_OF_INTEGERS': [1, 2, 3],
            '_MY_ARRAY_OF_STRINGS': ['string1', 'string2', 'string3'],
            '_PACKAGES': [
                {'id': 'identifier', 'name': 'Package 1', 'other': 1},
                {'id': 'identifier', 'name': 'Package 2', 'other': 1}
            ],
            '_LIST_PACKAGES': [
                {'id': 'adobereader',
                 'service': 'soft_adobereader',
                 'version': '3.0.0'},
                {'id': 'cwrsync',
                 'service': 'soft_cwrsync',
                 'version': '3.1.2'},
                {'id': 'HomeMaison',
                 'service': 'HomeMaison',
                 'version': '0.1.0'},
                {'id': 'Inventory',
                 'service': 'soft_Inventory',
                 'version': '4.0.4'}
            ],
        }
        self.assertEqual(expected, test_host_0['customs'])
        # ----------

        # ----------
        # Create host service variables - unknown service
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",

            "services": [
                {
                    "name": "test_service",
                    "variables": {
                        'test1': 'string',
                        'test2': 1,
                        'test3': 5.0
                    },
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['test_host_0 is alive :)'],
            '_issues': ["Requested service 'test_host_0/test_service' does not exist. "
                         "Note that service creation is not allowed."]
        })
        # ----------

        # ----------
        # Create host service variables
        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        host = resp['_items'][0]
        # Get services data to confirm update
        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_0'})})
        resp = response.json()
        service = resp['_items'][0]
        print(("My service: %s" % service))

        # u'customs': {u'_TEMPLATE': u'generic', u'_ICON_IMAGE_ALT': u'icon alt string',
        #              u'_CUSTNAME': u'custvalue', u'_DISPLAY_NAME': u'test_ok_0',
        #              u'_ICON_IMAGE': u'../../docs/images/tip.gif?host=$HOSTNAME$&srv=$SERVICEDESC$'},
        # u'ls_attempt': 0, u'trigger_name': u'', u'service_dependencies': [], u'_updated': u'Fri, 17 Nov 2017 05:24:37 GMT', u'duplicate_foreach': u'', u'poller_tag': u'None', u'ls_last_time_unreachable': 0, u'ls_state_type': u'HARD', u'_id': u'5a0e729506fd4b062fc8ee2b', u'business_rule_output_template': u''}
        #
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",

            "services": [
                {
                    "name": "test_ok_0",
                    "variables": {
                        'test1': 'string',
                        'test2': 1,
                        'test3': 5.0,
                        'test5': 'service specific'
                    },
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "Service 'test_host_0/test_ok_0' unchanged."],
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        host = resp['_items'][0]
        # Get services data to confirm update
        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_0'})})
        resp = response.json()
        service = resp['_items'][0]
        # The service still had a variable _CUSTNAME and it inherits from all the host variables
        expected = {
            # u'_DISPLAY_NAME': u'test_ok_0',
            '_DISPLAY_NAME': ['test_host_0', 'test_ok_0'],
            '_TEMPLATE': 'generic',
            '_ICON_IMAGE': '../../docs/images/tip.gif?host=$HOSTNAME$&srv=$SERVICEDESC$',
            '_ICON_IMAGE_ALT': 'icon alt string',
            '_CUSTNAME': 'custvalue',
            '_TEST3': 5.0, '_TEST2': 1, '_TEST1': 'string',
            '_TEST5': 'service specific'
        }
        self.assertEqual(expected, service['customs'])
        # ----------

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    @pytest.mark.skip("Disabled feature - no more backend host update for passive/active checks")
    def test_module_zzz_host_enable_disable(self):
        """Test the module /host API - enable / disable active / passive checks - manage unchanged
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # No feedback
            'give_feedback': '0',
            # Give result data
            'give_result': '1',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get('http://127.0.0.1:5000/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        # ---

        # Do not allow GET request on /host - not yet authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # Update host variables - empty variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": "",
            "passive_checks_enabled": ""
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # ----------
        # Host does not exist
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "unknown_host",
            "active_checks_enabled": True,
            "passive_checks_enabled": True
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['unknown_host is alive :)'],
            '_issues': ["Requested host 'unknown_host' does not exist"]})

        # ----------
        # Enable all checks
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": True,
            "passive_checks_enabled": True
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' unchanged."]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        self.assertTrue(dummy_host['active_checks_enabled'])
        self.assertTrue(dummy_host['passive_checks_enabled'])
        # ----------

        # ----------
        # Enable all checks - again!
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": True,
            "passive_checks_enabled": True
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)', "Host 'test_host_0' unchanged."]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        self.assertTrue(dummy_host['active_checks_enabled'])
        self.assertTrue(dummy_host['passive_checks_enabled'])
        # ----------

        # ----------
        # Disable all checks
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": False,
            "passive_checks_enabled": False
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                'Host test_host_0 active checks will be disabled.',
                'Sent external command: DISABLE_HOST_CHECK;test_host_0.',
                'Host test_host_0 passive checks will be disabled.',
                'Sent external command: DISABLE_PASSIVE_HOST_CHECKS;test_host_0.',
                "Host 'test_host_0' updated."
            ]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        self.assertFalse(dummy_host['active_checks_enabled'])
        self.assertFalse(dummy_host['passive_checks_enabled'])
        # ----------

        # ----------
        # Mixed
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": True,
            "passive_checks_enabled": False
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                'Host test_host_0 active checks will be enabled.',
                'Sent external command: ENABLE_HOST_CHECK;test_host_0.',
                "Host 'test_host_0' updated."
            ]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        self.assertTrue(dummy_host['active_checks_enabled'])
        self.assertFalse(dummy_host['passive_checks_enabled'])
        # ----------

        # ----------
        # Mixed
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": False,
            "passive_checks_enabled": True
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                'Host test_host_0 active checks will be disabled.',
                'Sent external command: DISABLE_HOST_CHECK;test_host_0.',
                'Host test_host_0 passive checks will be enabled.',
                'Sent external command: ENABLE_PASSIVE_HOST_CHECKS;test_host_0.',
                "Host 'test_host_0' updated."
            ]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        self.assertFalse(dummy_host['active_checks_enabled'])
        self.assertTrue(dummy_host['passive_checks_enabled'])
        # ----------

        # ----------
        # Enable / Disable all host services - unknown services
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": False,
            "passive_checks_enabled": True,
            "services": [
                {
                    "name": "test_service",
                    "active_checks_enabled": True,
                    "passive_checks_enabled": True,
                },
                {
                    "name": "test_service2",
                    "active_checks_enabled": False,
                    "passive_checks_enabled": False,
                },
                {
                    "name": "test_service3",
                    "active_checks_enabled": True,
                    "passive_checks_enabled": False,
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'ERR',
            '_result': ['test_host_0 is alive :)',
                         "Host 'test_host_0' unchanged."],
            '_issues': ["Requested service 'test_host_0/test_service' does not exist",
                         "Requested service 'test_host_0/test_service2' does not exist",
                         "Requested service 'test_host_0/test_service3' does not exist"]
        })
        # ----------

        # ----------
        # Enable / Disable all host services
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": False,
            "passive_checks_enabled": True,
            "services": [
                {
                    "name": "test_ok_0",
                    "active_checks_enabled": True,
                    "passive_checks_enabled": True,
                },
                {
                    "name": "test_ok_1",
                    "active_checks_enabled": False,
                    "passive_checks_enabled": False,
                },
                {
                    "name": "test_ok_2",
                    "active_checks_enabled": True,
                    "passive_checks_enabled": False,
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        print(result)
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                'Service test_host_0/test_ok_0 active checks will be enabled.',
                'Sent external command: ENABLE_SVC_CHECK;test_host_0;test_ok_0.',
                'Service test_host_0/test_ok_0 passive checks will be enabled.',
                'Sent external command: ENABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_0.',
                "Service 'test_host_0/test_ok_0' updated",
                'Service test_host_0/test_ok_1 active checks will be disabled.',
                'Sent external command: DISABLE_SVC_CHECK;test_host_0;test_ok_1.',
                'Service test_host_0/test_ok_1 passive checks will be disabled.',
                'Sent external command: DISABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_1.',
                "Service 'test_host_0/test_ok_1' updated",
                'Service test_host_0/test_ok_2 active checks will be enabled.',
                'Sent external command: ENABLE_SVC_CHECK;test_host_0;test_ok_2.',
                'Service test_host_0/test_ok_2 passive checks will be disabled.',
                'Sent external command: DISABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_2.',
                "Service 'test_host_0/test_ok_2' updated",
                "Host 'test_host_0' unchanged."
            ]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        host = resp['_items'][0]
        self.assertFalse(host['active_checks_enabled'])
        self.assertTrue(host['passive_checks_enabled'])
        # Get services data to confirm update
        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_0'})})
        resp = response.json()
        service = resp['_items'][0]
        self.assertTrue(service['active_checks_enabled'])
        self.assertTrue(service['passive_checks_enabled'])

        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_1'})})
        resp = response.json()
        service = resp['_items'][0]
        self.assertFalse(service['active_checks_enabled'])
        self.assertFalse(service['passive_checks_enabled'])

        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_2'})})
        resp = response.json()
        service = resp['_items'][0]
        self.assertTrue(service['active_checks_enabled'])
        self.assertFalse(service['passive_checks_enabled'])
        # ----------

        # Logout

        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "active_checks_enabled": False,
            "passive_checks_enabled": True,
            "services": [
                {
                    "name": "test_ok_0",
                    "active_checks_enabled": False,
                    "passive_checks_enabled": False,
                },
                {
                    "name": "test_ok_1",
                    "active_checks_enabled": True,
                    "passive_checks_enabled": True,
                },
                {
                    "name": "test_ok_2",
                    "active_checks_enabled": False,
                    "passive_checks_enabled": True,
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        print(result)
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'test_host_0 is alive :)',
                'Service test_host_0/test_ok_0 active checks will be disabled.',
                'Sent external command: DISABLE_SVC_CHECK;test_host_0;test_ok_0.',
                'Service test_host_0/test_ok_0 passive checks will be disabled.',
                'Sent external command: DISABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_0.',
                "Service 'test_host_0/test_ok_0' updated",

                'Service test_host_0/test_ok_1 active checks will be enabled.',
                'Sent external command: ENABLE_SVC_CHECK;test_host_0;test_ok_1.',
                'Service test_host_0/test_ok_1 passive checks will be enabled.',
                'Sent external command: ENABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_1.',
                "Service 'test_host_0/test_ok_1' updated",

                'Service test_host_0/test_ok_2 active checks will be disabled.',
                'Sent external command: DISABLE_SVC_CHECK;test_host_0;test_ok_2.',
                'Service test_host_0/test_ok_2 passive checks will be enabled.',
                'Sent external command: ENABLE_PASSIVE_SVC_CHECKS;test_host_0;test_ok_2.',
                "Service 'test_host_0/test_ok_2' updated",

                "Host 'test_host_0' unchanged."
            ]
        })

        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_passive_active(self):
        """Test the module /host API - enable / disable active / passive checks - manage unchanged
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # No feedback
            'give_feedback': '1',
            'feedback_host': 'active_checks_enabled,check_interval,passive_checks_enabled,freshness_threshold',
            # Give result data
            'give_result': '1',
            # Do not allow host/service creation
            'allow_host_creation': '1',
            'allow_service_creation': '1',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        dummy_host = resp['_items'][0]
        # ---

        # Do not allow GET request on /host - not yet authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # 1 - Request to create an host - with some specific properties
        data = {
            "name": "a_very_new_host",
            "template": {
                "active_checks_enabled": "1",
                "passive_checks_enabled": "1",
                "freshness_threshold": 120,
                "check_freshness": "1",
                "alias": "My very new host ...",
                "check_period": "24x7"
            }
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': [
                'a_very_new_host is alive :)',
                "Requested host 'a_very_new_host' does not exist.",
                "Requested host 'a_very_new_host' created."
            ],
            '_feedback': {
                'name': 'a_very_new_host',
                'passive_checks_enabled': True,
                'active_checks_enabled': True,
                'check_interval': 5,
                'freshness_threshold': 120
            }
        })

        # Get new host to confirm creation
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'a_very_new_host'})})
        resp = response.json()
        new_host_1 = resp['_items'][0]
        self.assertEqual('a_very_new_host', new_host_1['name'])
        self.assertEqual(new_host_1['alias'], "My very new host ...")
        self.assertNotEqual(new_host_1['check_period'], None)
        self.assertEqual(self.realmAll_id, new_host_1['_realm'])

        self.assertEqual(True, new_host_1['passive_checks_enabled'])
        self.assertEqual(True, new_host_1['active_checks_enabled'])
        self.assertEqual(5, new_host_1['check_interval'])
        self.assertEqual(120, new_host_1['freshness_threshold'])

        # 2 - Simple host heartbeat - nothing special to report ;)
        data = {
            "name": "a_very_new_host"
        }
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['a_very_new_host is alive :)'],
            '_feedback': {
                'name': 'a_very_new_host',
                'passive_checks_enabled': True,
                'active_checks_enabled': True,
                'check_interval': 5,
                'freshness_threshold': 120
            }
        })


        # 3 - host configuration changes in Alignak
        # Update hosts's parameters
        headers = {'Content-Type': 'application/json', 'If-Match': new_host_1['_etag']}
        data = {
            'passive_checks_enabled': False,
            'active_checks_enabled': False,
            "freshness_threshold": 360
        }
        resp = requests.patch(self.endpoint + '/host/' + new_host_1['_id'],
                              json=data, headers=headers, auth=self.auth)
        resp = resp.json()
        assert resp['_status'] == 'OK'

        # Host heartbeat
        response = session.patch(self.ws_endpoint + '/host/a_very_new_host',
                                 json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['a_very_new_host is alive :)'],
            '_feedback': {
                'name': 'a_very_new_host',
                'passive_checks_enabled': False,
                'active_checks_enabled': False,
                'check_interval': 5,
                'freshness_threshold': 360
            }
        })
        # Response contains host backend data

        # Host heartbeat with configuration data
        data = {
            "active_checks_enabled": "1",
            "passive_checks_enabled": "1",
            "freshness_threshold": 120
        }
        response = session.patch(self.ws_endpoint + '/host/a_very_new_host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['a_very_new_host is alive :)'],
            '_feedback': {
                'name': 'a_very_new_host',
                'passive_checks_enabled': False,
                'active_checks_enabled': False,
                'check_interval': 5,
                'freshness_threshold': 360
            }
        })
        # Response always contains host backend data!
        # Host is data-slave for the host configuration !

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_no_feedback(self):
        """Test the module /host API * create/update custom variables * no feedback in the response
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Do not give feedback data
            'give_feedback': '0',
            # Give result data
            'give_result': '1',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Errors for unknown host/service
            'ignore_unknown_host': '0',
            'ignore_unknown_service': '0',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get('http://127.0.0.1:5000/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # ---

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # You must have parameters when POSTing on /host
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_error'], 'You must send parameters on this endpoint.')

        # Update host variables - empty variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": "",
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)']
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl',
            '_OSTYPE': 'gnulinux'
        }
        self.assertEqual(expected, test_host_0['customs'])

        # ----------
        # Host does not exist
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "unknown_host",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['unknown_host is alive :)'],
                                  '_issues': ["Requested host 'unknown_host' does not exist. "
                                               "Note that host creation is not allowed."]})


        # ----------
        # Create host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ["test_host_0 is alive :)",
                         "Host 'test_host_0' updated."]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        expected = {
            # u'_DISPLAY_NAME': u'test_host_0',
            '_TEMPLATE': 'generic',
            '_OSLICENSE': 'gpl', '_OSTYPE': 'gnulinux',
            '_TEST3': 5.0, '_TEST2': 1, '_TEST1': 'string'
        }
        self.assertEqual(expected, test_host_0['customs'])

        # ----------
        # Create host service variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",

            "services": [
                {
                    "name": "test_ok_0",
                    "variables": {
                        'test1': 'string',
                        'test2': 1,
                        'test3': 5.0,
                        'test5': 'service specific'
                    },
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
            '_result': ['test_host_0 is alive :)',
                         "Service 'test_host_0/test_ok_0' updated"]
        })

        # Get host data to confirm update
        response = requests.get(self.endpoint + '/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        host = resp['_items'][0]
        # Get services data to confirm update
        response = requests.get('http://127.0.0.1:5000/service', auth=self.auth,
                                params={'where': json.dumps({'host': host['_id'],
                                                             'name': 'test_ok_0'})})
        resp = response.json()
        service = resp['_items'][0]
        # The service still had a variable _CUSTNAME and it inherits from the host variables
        expected = {
            # u'_DISPLAY_NAME': u'test_ok_0',
            '_DISPLAY_NAME': ['test_host_0', 'test_ok_0'],
            '_TEMPLATE': 'generic',
            '_ICON_IMAGE': '../../docs/images/tip.gif?host=$HOSTNAME$&srv=$SERVICEDESC$',
            '_ICON_IMAGE_ALT': 'icon alt string',
            '_CUSTNAME': 'custvalue',
            '_TEST3': 5.0, '_TEST2': 1, '_TEST1': 'string',
            '_TEST5': 'service specific'
        }
        self.assertEqual(expected, service['customs'])
        # ----------

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_no_result(self):
        """Test the module /host API * create/update custom variables * no result in the response
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': 0,
            # Do not give feedback data
            'give_feedback': 0,
            # Do not give result data
            'give_result': 0,
            # Do not allow host/service creation
            'allow_host_creation': 0,
            'allow_service_creation': 0,
            # Errors for unknown host/service
            'ignore_unknown_host': 0,
            'ignore_unknown_service': 0,
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.show_logs()
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get('http://127.0.0.1:5000/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # ---

        # Do not allow GET request on /host - not authorized
        response = requests.get(self.ws_endpoint + '/host')
        self.assertEqual(response.status_code, 401)

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # You must have parameters when POSTing on /host
        headers = {'Content-Type': 'application/json'}
        data = {}
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'ERR')
        self.assertEqual(result['_error'], 'You must send parameters on this endpoint.')

        # Update host variables - empty variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": "",
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'OK'})

        # ----------
        # Host does not exist
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "unknown_host",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'ERR',
                                  '_result': ['unknown_host is alive :)'],
                                  '_issues': ["Requested host 'unknown_host' does not exist. "
                                               "Note that host creation is not allowed."]})


        # ----------
        # Create host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
        })

        # ----------
        # Create host service variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",

            "services": [
                {
                    "name": "test_ok_0",
                    "variables": {
                        'test1': 'string',
                        'test2': 1,
                        'test3': 5.0,
                        'test5': 'service specific'
                    },
                },
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_status': 'OK',
        })
        # ----------

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()

    def test_module_zzz_host_ignore(self):
        """Test the module /host API * ignore unknown host or service
        :return:
        """
        self.setup_with_file('./cfg/cfg_default.cfg', unit_test=False)
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'web-services',
            'module_types': 'web-services',
            'python_name': 'alignak_module_ws',
            # Alignak backend
            'alignak_backend': 'http://127.0.0.1:5000',
            'username': 'admin',
            'password': 'admin',
            # Do not set a timestamp in the built external commands
            'set_timestamp': '0',
            # Do not give feedback data
            'give_feedback': '0',
            # Do not give result data
            'give_result': '1',
            # Do not allow host/service creation
            'allow_host_creation': '0',
            'allow_service_creation': '0',
            # Ignore unknown host/service
            'ignore_unknown_host': '1',
            'ignore_unknown_service': '1',
            # Set Arbiter address as empty to not poll the Arbiter else the test will fail!
            'alignak_host': '',
            'alignak_port': 7770,
        })

        # Create a receiver daemon
        args = {'env_file': '', 'daemon_name': 'receiver-master'}
        self._receiver_daemon = Receiver(**args)

        # Create the modules manager for the daemon
        self.modulemanager = ModulesManager(self._receiver_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        my_module = self.modulemanager.instances[0]

        # Clear logs
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module logs
        self.assert_log_match("Trying to initialize module: web-services", 0)
        self.assert_log_match("Starting external module web-services", 1)
        self.assert_log_match("Starting external process for module web-services", 2)
        self.assert_log_match("web-services is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        time.sleep(1)

        # Get host data to confirm backend update
        # ---
        response = requests.get('http://127.0.0.1:5000/host', auth=self.auth,
                                params={'where': json.dumps({'name': 'test_host_0'})})
        resp = response.json()
        test_host_0 = resp['_items'][0]
        # ---

        session = requests.Session()

        # Login with username/password (real backend login)
        headers = {'Content-Type': 'application/json'}
        params = {'username': 'admin', 'password': 'admin'}
        response = session.post(self.ws_endpoint + '/login', json=params, headers=headers)
        assert response.status_code == 200
        resp = response.json()

        # ----------
        # Create host variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "unknown_host",
            "variables": {
                'test1': 'string',
                'test2': 1,
                'test3': 5.0
            },
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {'_status': 'OK',
                                  '_issues': [],
                                  '_result': ["Requested host 'unknown_host' does not exist"]})

        # ----------
        # Create host service variables
        headers = {'Content-Type': 'application/json'}
        data = {
            "name": "test_host_0",

            "services": [
                {
                    "name": "unknown_service",
                    "variables": {
                        'test1': 'string',
                        'test2': 1,
                        'test3': 5.0,
                        'test5': 'service specific'
                    }
                }
            ]
        }
        self.assertEqual(my_module.received_commands, 0)
        response = session.patch(self.ws_endpoint + '/host', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result, {
            '_result': ['test_host_0 is alive :)',
                         "Requested service 'test_host_0/unknown_service' does not exist. Note that service creation is not allowed."],
            # u'_issues': [u"Requested service 'test_host_0/unknown_service' does not exist. Note that service creation is not allowed."],
            '_status': 'OK'
        })
        # ----------

        # Logout
        response = session.get(self.ws_endpoint + '/logout')
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertEqual(result['_status'], 'OK')
        self.assertEqual(result['_result'], 'Logged out')

        self.modulemanager.stop_all()
