import pipef


def test_exposes_a_version():
    assert isinstance(pipef.__version__, str)
    assert pipef.__version__
