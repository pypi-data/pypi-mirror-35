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

import re
import os
import time
import pytest

from .alignak_test import AlignakTest
from alignak.modulesmanager import ModulesManager
from alignak.objects.module import Module
from alignak.basemodule import BaseModule
from alignak.brok import Brok

# Set environment variable to ask code Coverage collection
os.environ['COVERAGE_PROCESS_START'] = '.coveragerc'

import alignak_module_nsca


class TestModules(AlignakTest):
    """
    This class contains the tests for the module
    """

    def test_module_loading(self):
        """
        Test module loading

        Alignak module loading

        :return:
        """
        self.setup_with_file('./cfg/alignak.cfg')
        self.assertTrue(self.conf_is_correct)
        self.show_configuration_logs()

        # No arbiter modules created
        modules = [m.module_alias for m in self._arbiter.link_to_myself.modules]
        self.assertListEqual(modules, [])

        # No broker modules
        modules = [m.module_alias for m in self._broker_daemon.modules]
        self.assertListEqual(modules, [])

        # No scheduler modules
        modules = [m.module_alias for m in self._scheduler_daemon.modules]
        self.assertListEqual(modules, ['inner-retention'])

        # A receiver module
        modules = [m.module_alias for m in self._receiver.modules]
        self.assertListEqual(modules, ['nsca'])

    def test_module_manager(self):
        """
        Test if the module manager manages correctly all the modules
        :return:
        """
        self.setup_with_file('./cfg/alignak.cfg')
        self.assertTrue(self.conf_is_correct)
        self.clear_logs()

        # Create an Alignak module
        mod = Module({
            'module_alias': 'nsca',
            'module_types': 'nsca',
            'python_name': 'alignak_module_nsca'
        })

        # Create the modules manager for a daemon type
        self.modulemanager = ModulesManager(self._broker_daemon)

        # Load an initialize the modules:
        #  - load python module
        #  - get module properties and instances
        self.modulemanager.load_and_init([mod])

        # Loading module nsca
        print("Load and init")
        self.show_logs()
        i=0
        self.assert_log_match(re.escape(
            "Importing Python module 'alignak_module_nsca' for nsca..."
        ), i)
        i += 1
        # Dict order is problematic :/
        # self.assert_log_match(re.escape(
        #     "Module properties: {'daemons': ['broker'], 'phases': ['running'], "
        #     "'type': 'nsca', 'external': True}"
        # ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Imported 'alignak_module_nsca' for nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Loaded Python module 'alignak_module_nsca' (nsca)"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Alignak starting module 'nsca'"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Give an instance of alignak_module_nsca for alias: nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "configuration, allowed hosts : '127.0.0.1'(5667), buffer length: 4096, "
            "payload length: -1, encryption: 0, max packet age: 30, "
            "check future packet: True, backlog: 10"
        ), i)

        time.sleep(1)
        # Reload the module
        print("Reload")
        self.modulemanager.load([mod])
        self.modulemanager.get_instances()
        #
        # Loading module nsca
        self.show_logs()
        i = 0
        self.assert_log_match(re.escape(
            "Importing Python module 'alignak_module_nsca' for nsca..."
        ), i)
        i += 1
        # self.assert_log_match(re.escape(
        #     "Module properties: {'daemons': ['broker'], 'phases': ['running'], "
        #     "'type': 'nsca', 'external': True}"
        # ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Imported 'alignak_module_nsca' for nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Loaded Python module 'alignak_module_nsca' (nsca)"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Alignak starting module 'nsca'"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Give an instance of alignak_module_nsca for alias: nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "configuration, allowed hosts : '127.0.0.1'(5667), buffer length: 4096, "
            "payload length: -1, encryption: 0, max packet age: 30, "
            "check future packet: True, backlog: 10"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Importing Python module 'alignak_module_nsca' for nsca..."
        ), i)
        i += 1
        # self.assert_log_match(re.escape(
        #     "Module properties: {'daemons': ['broker'], 'phases': ['running'], "
        #     "'type': 'nsca', 'external': True}"
        # ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Imported 'alignak_module_nsca' for nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Loaded Python module 'alignak_module_nsca' (nsca)"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Request external process to stop for nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "External process stopped."
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "Alignak starting module 'nsca'"
        ), i)
        i += 1
        # self.assert_log_match(re.escape(
        #     "Give an instance of alignak_module_nsca for alias: nsca"
        # ), i)
        # i += 1
        self.assert_log_match(re.escape(
            "Give an instance of alignak_module_nsca for alias: nsca"
        ), i)
        i += 1
        self.assert_log_match(re.escape(
            "configuration, allowed hosts : '127.0.0.1'(5667), buffer length: 4096, "
            "payload length: -1, encryption: 0, max packet age: 30, "
            "check future packet: True, backlog: 10"
        ), i)

        my_module = self.modulemanager.instances[0]

        # Get list of not external modules
        self.assertListEqual([], self.modulemanager.get_internal_instances())
        for phase in ['configuration', 'late_configuration', 'running', 'retention']:
            self.assertListEqual([], self.modulemanager.get_internal_instances(phase))

        # Get list of external modules
        self.assertListEqual([my_module], self.modulemanager.get_external_instances())
        for phase in ['configuration', 'late_configuration', 'retention']:
            self.assertListEqual([], self.modulemanager.get_external_instances(phase))
        for phase in ['running']:
            self.assertListEqual([my_module], self.modulemanager.get_external_instances(phase))

        # Clear nsca
        self.clear_logs()

        # Start external modules
        self.modulemanager.start_external_instances()

        # Starting external module nsca
        self.assert_log_match("Trying to initialize module: nsca", 0)
        self.assert_log_match("Starting external module nsca", 1)
        self.assert_log_match("Starting external process for module nsca", 2)
        self.assert_log_match("nsca is now started", 3)

        # Check alive
        self.assertIsNotNone(my_module.process)
        self.assertTrue(my_module.process.is_alive())

        # Clear nsca
        self.clear_logs()

        # Kill the external module (normal stop is .stop_process)
        my_module.kill()
        time.sleep(0.1)
        index = 0
        self.assert_log_match("Killing external module", index)
        index = index + 1
        # todo: This log is not expected! But it is probably because of the py.test ...
        # Indeed the receiver daemon that the module is attached to is receiving a SIGTERM !!!
        self.assert_log_match(re.escape("nsca is still living 10 seconds after a normal kill, I help it to die"), index)
        index = index + 1
        self.assert_log_match("External module killed", index)
        index = index + 1

        # Should be dead (not normally stopped...) but we still know a process for this module!
        self.assertIsNotNone(my_module.process)

        # Nothing special ...
        self.modulemanager.check_alive_instances()
        self.assert_log_match("The external module nsca died unexpectedly!", index)
        index = index + 1
        self.assert_log_match("Setting the module nsca to restart", index)
        index = index + 1

        # # Try to restart the dead modules
        # self.modulemanager.try_to_restart_deads()
        # self.assert_log_match("Trying to restart module: nsca", index)
        # index = index +1
        # self.assert_log_match("Too early to retry initialization, retry period is 5 seconds", index)
        # index = index +1
        #
        # # In fact it's too early, so it won't do it
        # # The module instance is still dead
        # self.assertFalse(my_module.process.is_alive())

        # So we lie, on the restart tries ...
        my_module.last_init_try = -5
        self.modulemanager.check_alive_instances()
        self.modulemanager.try_to_restart_deads()
        self.assert_log_match("Trying to restart module: nsca", index)
        index = index +1
        self.assert_log_match("Trying to initialize module: nsca", index)
        index = index +1
        self.assert_log_match("Restarting nsca...", index)
        index = index +1

        # The module instance is now alive again
        self.assertTrue(my_module.process.is_alive())
        self.assert_log_match("Starting external process for module nsca", index)
        index = index + 1
        self.assert_log_match("nsca is now started", index)
        index = index + 1

        # There is nothing else to restart in the module manager
        self.assertEqual([], self.modulemanager.to_restart)

        # Clear nsca
        self.clear_logs()

        # Let the module start and then kill it again
        time.sleep(3.0)
        my_module.kill()
        # time.sleep(5.0)
        self.show_logs()
        print("My module PID 2: %s" % my_module.process.pid)
        time.sleep(0.2)
        self.assertFalse(my_module.process.is_alive())
        index = 0
        self.assert_log_match("Killing external module", index)
        index = index +1
        # # todo: This log is not expected! But it is probably because of the py.test ...
        # # Indeed the receiver daemon that the module is attached to is receiving a SIGTERM !!!
        # self.assert_log_match(re.escape("'web-services' is still living 10 seconds after a normal kill, I help it to die"), index)
        # index = index +1
        self.assert_log_match("External module killed", index)
        index = index +1

        # The module is dead but the modules manager do not know yet!
        self.modulemanager.check_alive_instances()
        self.assert_log_match("The external module nsca died unexpectedly!", index)
        index = index +1
        self.assert_log_match("Setting the module nsca to restart", index)
        index = index +1

        self.modulemanager.try_to_restart_deads()
        self.assert_log_match("Trying to restart module: nsca", index)
        index = index +1
        self.assert_log_match("Too early to retry initialization, retry period is 5 seconds", index)
        index = index +1

        # In fact it's too early, so it won't do it
        # The module instance is still dead
        self.assertFalse(my_module.process.is_alive())

        # So we lie, on the restart tries ...
        my_module.last_init_try = -5
        self.modulemanager.check_alive_instances()
        self.modulemanager.try_to_restart_deads()
        self.assert_log_match("Trying to restart module: nsca", index)
        index = index +1
        self.assert_log_match("Trying to initialize module: nsca", index)
        index = index +1
        self.assert_log_match("Restarting nsca...", index)
        index = index +1

        # The module instance is now alive again
        self.assertTrue(my_module.process.is_alive())
        self.assert_log_match("Starting external process for module nsca", index)
        index = index +1
        self.assert_log_match("nsca is now started", index)
        index = index +1
        time.sleep(1.0)
        print("My module PID: %s" % my_module.process.pid)

        # Clear nsca
        self.clear_logs()

        # And we clear all now
        self.modulemanager.stop_all()
        # Stopping module nsca

        index = 0
        self.assert_log_match("Shutting down modules...", index)
        index = index +1
        self.assert_log_match("Request external process to stop for nsca", index)
        index = index +1
        self.assert_log_match(re.escape("I'm stopping module 'nsca' (pid="), index)
        index = index +1
        # self.assert_log_match(re.escape("'nsca' is still living after a normal kill, I help it to die"), index)
        # index = index +1
        self.assert_log_match(re.escape("Killing external module (pid"), index)
        index = index +1
        self.assert_log_match(re.escape("External module killed"), index)
        index = index +1
        self.assert_log_match("External process stopped.", index)
        index = index +1

    def test_module_start_default(self):
        """Test the module initialization function, no parameters, using default
        :return:
        """
        # Obliged to call to get a self.logger...
        self.setup_with_file('./cfg/alignak.cfg')
        self.assertTrue(self.conf_is_correct)

        # Clear nsca
        self.clear_logs()

        # -----
        # Default initialization
        # -----
        # Create an Alignak module
        mod = Module({
            'module_alias': 'nsca',
            'module_types': 'passive',
            'python_name': 'alignak_module_nsca'
        })

        instance = alignak_module_nsca.get_instance(mod)
        self.assertIsInstance(instance, BaseModule)
        self.show_logs()

        # self.assert_log_match(
        #     re.escape("Give an instance of alignak_module_nsca for alias: nsca"), 0)
        self.assert_log_match(re.escape(
            "Give an instance of alignak_module_nsca for alias: nsca"
        ), 0)
        self.assert_log_match(re.escape(
            "configuration, allowed hosts : '127.0.0.1'(5667), buffer length: 4096, "
            "payload length: -1, encryption: 0, max packet age: 30, "
            "check future packet: True, backlog: 10"
        ), 1)
