import pytest

class TestClass:
    @pytest.fixture() #Decorator,Fixture
    def setup(self):
        print("Open Aplpication") # Excecute once before every test method
        yield
        print("Closing Browser") # Excecute once after every test method bcoz of yield

    def test_Login(self,setup):
        print("test_method1")

    def test_Search(self,setup):
        print("test_method2")

    def test_AdvancedSearch(self,setup):
        print("test_method3")