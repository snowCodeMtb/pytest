from hello import hello


def test_default():
    assert hello() == "hello, world"

def test_argument():
    # consider one test
    for name in ["mcs", "vic", "ron"]:
        assert hello("Mcs") == "hello, Mcs"
    