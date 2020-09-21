import pytest

def pytest_generate_tests(metafunc):
    if 'abc' in metafunc.fixturenames:
        metafunc.parametrize('imo', [9632179, 9247455, 9595321])