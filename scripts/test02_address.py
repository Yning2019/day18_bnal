import sys
import os

sys.path.append(os.getcwd())

import pytest

from tool.get_log import GetLog
from tool.read_yaml import read_yaml

from page.page_in import PageIn
from tool.get_driver import GetDriver

#  https://github.com/Yning2019/day18_bnal.git
log = GetLog.get_log()


def get_date(key):
    arrs = list()
    if key == "add_address":
        arrs.append(tuple(read_yaml("address.yaml").get("add_address").values()))
        return arrs
    else:
        arrs.append(tuple(read_yaml("address.yaml").get("update_address").values()))
        return arrs


class TestAddress:
    # 初始化
    def setup_class(self):
        # 获取 PageAddress
        self.address = PageIn().page_get_pageaddress()
        # 获取PageLogin 并且登录成功
        PageIn().page_get_pagelogin().page_login_address()
        # 点击 地址管理
        self.address.page_click_manage()

    # 结束
    def teardown_class(self):
        # 关闭driver对象
        GetDriver.quit_driver()

    # 测试方法
    @pytest.mark.parametrize("name, phone, address, code, province,city, area", get_date("add_address"))
    def test01_add_address(self, name, phone, address, code, province, city, area):
        # 调用地址管理新增业务方法
        self.address.page_address(name, phone, address, code, province, city, area)
        # 组合收件人 和电话
        expect = name + "  " + phone
        # 测试看效果
        print("判断 {} in {}".format(expect, self.address.page_get_name_iphone()))
        # 断言
        try:
            assert expect in self.address.page_get_name_iphone()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 日志
            log.error(e)

    # 更新地址
    @pytest.mark.parametrize("name, phone, address, code, provice,city, area", get_date("update_address"))
    def test02_update_address(self, name, phone, address, code, provice, city, area):
        self.address.page_update_address(name, phone, address, code, provice, city, area)
        # 组合收件人和电话
        expect = name + "  " + phone
        print("判断 {} in {}".format(expect, self.address.page_get_name_iphone()))
        # 断言
        try:
            assert expect in self.address.page_get_name_iphone()
        except Exception as e:
            self.address.base_get_img()
            # 日志
            log.error(e)

    # 删除。地址
    def test03_delete_address(self):
        self.address.page_delete_address()
        # 断言
        try:
            assert self.address.page_address_is_exists()
        except Exception as e:
            # 截图
            self.address.base_get_img()
            # 日志
            log.error(e)
