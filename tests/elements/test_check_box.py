import pytest
from pytest import mark


@mark.C0007
@pytest.mark.skip
@mark.check_box
def test_check_box(driver):
    pass
