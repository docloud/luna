# coding=utf8

from luna import app
from luna.init import init_app


def test_api_init():
    assert app
    init_app()


if __name__ == '__main__':
    import IPython

    IPython.embed()
