import pytest

class TestClass:

    @pytest.fixture()
    def setup(self):
        print("Launching Browser")
        print("Open Aplpication")

    def test_Login(self,setup):
        print("test_method1")

    def test_Search(self,setup):
        print("test_method2")

    def test_AdvancedSearch(self,setup):
        print("test_method3")