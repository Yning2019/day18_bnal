from selenium.webdriver.common.by import By

"""以下为登录模块配置数据"""
# 点击我
login_me = By.ID, "com.yunmall.lc:id/tab_me"
# 点击已有账号去登录
login_username_link = By.ID, "com.yunmall.lc:id/textView1"
# 用户名
login_username = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 密码
login_pwd = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 登录按钮
login_btn = By.ID, "com.yunmall.lc:id/logon_button"
# 昵称
login_nickname = By.ID, "com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
# 消息推送
login_send_msg = By.ID, "com.yunmall.lc:id/setting_notification"
# 修改密码
login_modify_pwd = By.ID, "com.yunmall.lc:id/setting_modify_pwd"
# 退出
login_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 确认退出
login_logout_ok = By.ID, "com.yunmall.lc:id/ymdialog_right_button"
# 关闭弹窗
login_close_alert = By.ID, "com.yunmall.lc:id/img_close"

"""以下为地址管理配置数据"""
# 地址管理
address_manage = By.ID, "com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_new_address = By.ID, "com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name = By.ID, "com.yunmall.lc:id/address_receipt_name"
# 手机号
address_add_phone = By.ID, "com.yunmall.lc:id/address_add_phone"
# 所在地区
address_area = By.ID, "com.yunmall.lc:id/address_province"
# 详细地址
address_detail_address = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_post_code = By.ID, "com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default_address = By.ID, "com.yunmall.lc:id/address_default"
# 保存
address_save = By.ID, "com.yunmall.lc:id/button_send"
# 收件人 电话
address_name_phone = By.ID, "com.yunmall.lc:id/receipt_name"
# --------------------------直辖市--------------------------------------

# 更新地址
# 点击编辑
address_put_edit = By.ID, "com.yunmall.lc:id/ymtitlebar_right_btn"
# 点击修改
address_modify = By.ID, "com.yunmall.lc:id/modify"
# 点击删除
address_delete = By.ID, "com.yunmall.lc:id/delete"
# 点击确认删除
address_confirm_btn = By.ID, "com.yunmall.lc:id/ymdialog_left_button"
# 收件人：com.yunmall.lc:id/receipt_name  收货地址：com.yunmall.lc:id/receipt_address
