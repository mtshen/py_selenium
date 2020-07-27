from TestBase import base.TestBase
from threading import Timer


class ChangeLang(TestBase):
  def __init__(self):
    super().__init__()
    self.name = '切换语言'

  def waitReady(self, resolve, reject):

    # 只能在登陆页面进行该步骤
    self.appointUrl = 'static/auth-manage/#/login'

    resolve()

def prinTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime,(inc,))
    t.start()

printTime(2)


# 选择语言, 只有在登陆页面才能进行选择语言控制
# def selectLang(driver, value):
#   # TODO: 日志纪录
#   # TODO: 操作之前需要等待页面加载完成
#   # TODO: 操作结束后检查此步操作是否正常/通过页面数据
#   # 使用 driver.implicitly_wait 轮询做查询
#   driver.find_elements_by_css_selector(".ui-changeLang .el-input")[0].click()
#   selectItems = driver.find_elements_by_css_selector(".el-select-dropdown .el-select-dropdown__item")

#   driver.implicitly_wait(0.5)

#   for item in selectItems:
#     if item.text == value:
#       item.click()
#       break
#   return driver
