import pytest
from utilities.Logger import Logger
import logging


@pytest.mark.usefixtures("driver_setup")
# @pytest.mark.usefixtures("check_test_result")
class BaseTestClass:

    url = None
