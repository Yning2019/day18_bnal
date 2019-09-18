from page.page_address import PageAddress
from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()
    # 获取 登录页面对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)

    # 获取 地址管理页面对象
    def page_get_pageaddress(self):
        return PageAddress(self.driver)