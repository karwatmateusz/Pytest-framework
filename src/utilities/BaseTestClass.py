import pytest
from utilities.logger import Logger
import logging


@pytest.mark.usefixtures("driver_setup")
# @pytest.mark.usefixtures("take_screenshot")
class BaseTestClass:

    url = None
