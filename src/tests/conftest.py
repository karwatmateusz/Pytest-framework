import pytest


@pytest.fixture(scope="session", autouse=True)
def suite_starting():
    print("\n****** Regression suite started ******")
    yield
    print("\n****** Regression suite finished ******")