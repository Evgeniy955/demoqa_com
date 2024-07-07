import pytest
from pytest import mark

from utils.helper_methods import test_number


@test_number("07")
@pytest.mark.skip
@mark.check_box
def test_check_box(driver):
    pass
