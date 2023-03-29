import pytest


@pytest.fixture(scope="session", autouse=True)
def suite_starting():
    print("\nRegression suite started")
    yield
    print("\nRegression suite finished")
