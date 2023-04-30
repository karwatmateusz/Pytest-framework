import pytest
from utilities.Logger import Logger
import logging


@pytest.mark.usefixtures("driver_setup")
class BaseTestClass:
    url = None
