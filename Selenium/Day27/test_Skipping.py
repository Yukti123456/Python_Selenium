import  pytest
import sys

class Test_Login:
    def test_LoginGoogle(self):
        print("This is login by Google")
        assert 1 ==1

    @pytest.mark.skipif(sys.platform == "win32", reason="Not supported on Windows")
    def test_LoginInstagram(self):
        print("This is login by Instagram")
        assert 1 ==1

    def test_LoginWhatsapp(self):
        print("This is login by Whatsapp")
        assert 1 ==1

    def test_payment(self):
        payment_available = False

        if not payment_available:
            pytest.skip("Payment service is unavailable")

        assert True
    @pytest.mark.skip
    def test_SingupGoogle(self):
        print("This is login by Google")
        assert 1 ==1

    @pytest.mark.skip
    def test_SingupInstagram(self):
        print("This is login by Google")
        assert 1 ==1
    @pytest.mark.skip
    def test_SingupWhatsapp(self):
        print("This is login by Whatsapp")
        assert 1 ==1

