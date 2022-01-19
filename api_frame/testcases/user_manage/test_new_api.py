import allure
import pytest
from commons.parametrize_util import read_testcase_yaml
from commons.requests_util import RequestsUtil
from redloads.test import Test

@allure.epic("微信公众号接口自动化测试平台")
@allure.feature("用户管理模块")
class TestUserApi:

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/user_manage/wy_new.yaml'))
    @allure.story("网易新闻接口")
    def test_new(self, caseinfo):
        RequestsUtil(Test()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/user_manage/md5.yaml'))
    def test_md5(self, caseinfo):
        RequestsUtil(Test()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/user_manage/base64.yaml'))
    def test_base64(self, caseinfo):
        RequestsUtil(Test()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/user_manage/sign.yaml'))
    def test_sign(self, caseinfo):
        RequestsUtil(Test()).standard_yaml(caseinfo)

