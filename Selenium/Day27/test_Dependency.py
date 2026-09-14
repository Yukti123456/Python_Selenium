import pytest
class Test_Class:
    @pytest.mark.dependency()
    def test_openApp(self):
        assert 1==1
    @pytest.mark.dependency(depends=["Test_Class::test_openApp"])
    def test_login(self):
        assert 1==1
    @pytest.mark.dependency(depends=["Test_Class::test_login"])
    def test_search(self):
        assert False
    @pytest.mark.dependency(depends=["Test_Class::test_login","Test_Class::test_search"])
    def test_advsearch(self):
        assert 1==1
    @pytest.mark.dependency(depends=["Test_Class::test_openApp"])
    def test_logout(self):
        assert 1==1
