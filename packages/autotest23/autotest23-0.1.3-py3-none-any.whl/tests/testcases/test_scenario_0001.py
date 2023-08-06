"""
    Reminder: Make sure to use logger where it is needed. 
    These given log type will keep record in the log file.
    Logger Levels:
        * error
        * warning
        * critical
    [BRAIN STATION 23 | Design and Development: Md. Ariful Islam (BS1121)]
    """

import pytest
from django.test import LiveServerTestCase
from src.tests.drivercontroller.driver_controller import DriverController


# This fixture is default for a quick start If needed Tester can
# remove this fixture and call methods directly from the DriverController.
# to design own Test Scenerio and Test Cases.

@pytest.mark.usefixtures("suit_setup_and_tear_down")
class Testscenario0001(LiveServerTestCase, DriverController):
    """
            The classe and method names should start with Test...
            inside the test_scenerio_xxx.py file. If this naming convention
            is not followed properly these test scenerios/ test cases
            will not run with pytest command.
            """

    # Write your test case here.

    def test_case_0001(self):
        self.logger.warning("This auto-generated Test-Case is empty.")
        assert 1 == 1

    def test_case_0002(self):
        assert 1 == 1

