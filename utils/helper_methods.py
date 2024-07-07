import pytest


def test_number(*markers):
    def decorator(func):
        for marker in markers:
            func = pytest.mark.__getattr__(marker)(func)
        return func

    return decorator
