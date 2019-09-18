import sys
import os

sys.path.append(os.getcwd())
from tool.get_log import GetLog
from tool.read_yaml import read_yaml
import pytest

from page.page_in import PageIn
from tool.get_driver import GetDriver

log = GetLog.get_log()


def get_data():
    arrs = []
    for data in read_yaml("login.yaml").values():
        arrs.append(tuple(data.values()))
    return arrs


class TestLogin:
    # 初始化
    def setup_class(self):
        # 获取Page页面对象
        self.login = PageIn().page_get_pagelogin()
        # 关闭 弹窗
        self.login.page_close_alert()
        # 点击我
        self.login.page_click_me()
        # 点击已有账号，去登录
        self.login.page_click_username_link()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.quit_driver()

    # 登录测试方法
    @pytest.mark.parametrize("username, pwd, expect, success", get_data())
    def test_login(self, username, pwd, expect, success):
        # 调用登录业务方法
        self.login.page_login(username, pwd)
        if success:
            try:
                # 断言 昵称
                nickname = self.login.page_get_nickname()
                print("获取的昵称为：", nickname)
                assert self.login.page_get_nickname() == expect
            except Exception as e:
                # 截图 、日志
                self.login.base_get_img()
                log.error(e)
                # 抛异常
                raise
            finally:
                # 退出登录业务方法
                self.login.page_logout()
                # 点击 我
                self.login.page_click_me()
                # 点击 已有账号，去登录   用户名不能为空！
                self.login.page_click_username_link()
        else:
            try:
                # 断言 toast消息
                err_msg = self.login.page_get_toast(expect)
                print("获取的toast消息为：", err_msg)
                assert err_msg == expect
            except Exception as e:
                # 截图
                log.error(e)
                self.login.base_get_img()
                # 抛异常
                raise
