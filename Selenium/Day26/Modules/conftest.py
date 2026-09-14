import pytest

@pytest.fixture(scope="class")
def setup():
        print("Launching Browser")
        yield
        print("Closed Application")