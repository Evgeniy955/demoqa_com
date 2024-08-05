import allure
from allure import title
from pytest import mark


@mark.C0003
@title('check box test')
@allure.story("test check box test")
@allure.feature("check box test")
# @pytest.mark.skip
@mark.medium_priority
def test_check_box_test(driver):
    pass
