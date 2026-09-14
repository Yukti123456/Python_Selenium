import  pytest


class Test_ordering:
    @pytest.mark.run(order=2)
    def test_methodB(self):
        print("This is B")
        assert 1 ==1
    @pytest.mark.run(order=5)
    def test_methodE(self):
        print("This is E")
        assert 1 ==1

    @pytest.mark.run(order=3)
    def test_methodC(self):
        print("This is C")
        assert 1 ==1

    @pytest.mark.run(order=1)
    def test_methodA(self):
        print("This is A")
        assert 1 ==1

    @pytest.mark.run(order=4)
    def test_methodD(self):
        print("This is D")
        assert 1 ==1



