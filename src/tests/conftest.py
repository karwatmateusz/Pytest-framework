import pytest


@pytest.fixture(scope="session", autouse=False)
def suite_starting():
    print("\nRegression suite started")
    yield
    print("\nRegression suite finished")
