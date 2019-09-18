from time import sleep

import page
from base.base import Base
from tool.get_log import GetLog

log = GetLog.get_log()


class PageLogin(Base):
    # 关闭弹窗
    def page_close_alert(self):
        self.base_click(page.login_close_alert)

    # 点击 我
    def page_click_me(self):
        self.base_click(page.login_me)

    # 点击 已有账号，去登录
    def page_click_username_link(self):
        self.base_click(page.login_username_link)

    # 输入 用户名
    def page_input_username(self, username):
        self.base_input(page.login_username, username)

    # 输入 密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录 按钮
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    # 获取昵称 ->登录成功
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取 toast消息 ->登录失败
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 点击 设置
    def page_click_setting(self):
        self.base_click(page.login_setting)

    # 拖拽  消息推送->修改密码
    def page_drag_and_drop(self):
        self.base_drag_and_drop(page.login_send_msg, page.login_modify_pwd)

    # 点击退出
    def page_click_logout(self):
        self.base_click(page.login_logout)

    # 确认退出
    def page_click_logout_ok(self):
        self.base_click(page.login_logout_ok)

    # 退出登录业务方法
    def page_logout(self):
        log.info("正在执行退出登录业务方法")
        self.page_click_setting()
        self.page_drag_and_drop()
        self.page_click_logout()
        self.page_click_logout_ok()

    # 组合业务方法
    def page_login(self, username, pwd):
        log.info("【登录业务】正在执行登录操作，用户名：{} 密码：{}".format(username, pwd))
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()

    # 组合业务方法 成功：给地址管理使用
    def page_login_address(self, username="18333182751", pwd="yuanning123456"):
        self.page_close_alert()
        self.page_click_me()
        self.page_click_username_link()
        self.page_input_username(username)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
        sleep(2)  # 此处需要添加暂停时间，否则服务器容易500错误
        self.page_click_setting()
