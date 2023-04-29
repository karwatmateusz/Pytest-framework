import pytest
from utilities.Logger import Logger
from utilities.BaseTestClass import BaseTestClass
import logging


class TestAzure:
    log = Logger(logging.DEBUG)

    """Test that always pass created just to check azure pipeline"""

    @pytest.mark.azure
    def test_azure(self):
        self.log.info("some information to be logged")
        self.log.error("error message")
        assert 1 == 1
