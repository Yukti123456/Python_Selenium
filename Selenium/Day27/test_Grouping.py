import  pytest

class Test_Login:
    @pytest.mark.smoke
    def test_LoginGoogle(self):
        print("This is login by Google")
        assert 1 ==1

    @pytest.mark.smoke
    def test_LoginInstagram(self):
        print("This is login by Instagram")
        assert 1 ==1

    @pytest.mark.smoke
    def test_LoginWhatsapp(self):
        print("This is login by Whatsapp")
        assert 1 ==1

    @pytest.mark.regression
    def test_SingupGoogle(self):
        print("This is login by Google")
        assert 1 ==1

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_SingupInstagram(self):
        print("This is login by Google")
        assert 1 ==1

    @pytest.mark.regression
    def test_SingupWhatsapp(self):
        print("This is login by Whatsapp")
        assert 1 ==1


