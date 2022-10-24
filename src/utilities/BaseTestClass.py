import pytest


@pytest.mark.usefixtures("driver_setup")
@pytest.mark.usefixtures("attach_screenshot_on_fail")
class BaseTestClass:
    pass
