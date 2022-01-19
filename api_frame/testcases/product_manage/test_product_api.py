import allure
import pytest
from commons.parametrize_util import read_testcase_yaml
from commons.requests_util import RequestsUtil
from redloads.debug_talk import DebugTalk

@allure.epic("微信公众号接口自动化测试平台")
@allure.feature("商品管理模块")
class TestProductApi:

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("caseinfo",read_testcase_yaml('/testcases/product_manage/pm_get_token.yaml'))
    @allure.story("获取统一鉴权码接口")
    def test_get_token(self,caseinfo):
        allure.dynamic.title(caseinfo['name'])
        RequestsUtil(DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/product_manage/pm_create_flag.yaml'))
    def test_create_flag(self, caseinfo):
        RequestsUtil(DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/product_manage/pm_delete_flag.yaml'))
    def test_delete_flag(self, caseinfo):
        RequestsUtil(DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/product_manage/pm_select_flag.yaml'))
    def test_select_flag(self,caseinfo):
        RequestsUtil(DebugTalk()).standard_yaml(caseinfo)

    @pytest.mark.parametrize("caseinfo", read_testcase_yaml('/testcases/product_manage/pm_file_upload.yaml'))
    def test_file_upload(self,caseinfo):
       RequestsUtil(DebugTalk()).standard_yaml(caseinfo)




