import  pytest


class Test_ordering:
    @pytest.mark.second
    def test_methodB(self):
        print("This is B")
        assert 1 ==1
    @pytest.mark.fifth
    def test_methodE(self):
        print("This is E")
        assert 1 ==1

    @pytest.mark.third
    def test_methodC(self):
        print("This is C")
        assert 1 ==1

    @pytest.mark.first
    def test_methodA(self):
        print("This is A")
        assert 1 ==1

    @pytest.mark.fourth
    def test_methodD(self):
        print("This is D")
        assert 1 ==1



