import pytest
import logging
from utilities.Logger import Logger


@pytest.mark.usefixtures("driver_setup")
@pytest.mark.usefixtures("attach_screenshot_on_fail")
class BaseTestClass:

    url = None

    log = Logger(logging.DEBUG)
