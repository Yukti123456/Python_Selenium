import pytest

class TestLogin:
    def test_LoginEmail(self,setup):
        print("This is login by Email")
        assert  True==True
    def test_LoginFacebook(self,setup):
            print("This is login by Facebook")
            assert True == True
    def test_LoginGoogle(self,setup):
            print("This is login by Google")
            assert True == True