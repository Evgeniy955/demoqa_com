import pytest
from pytest import mark


@pytest.mark.skip
@mark.check_box_test
@mark.medium_priority
def test_check_box_test(driver):
    pass
