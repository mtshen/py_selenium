# 载入selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

# 启动chrome测试
def startChrome(url):
  driver = webdriver.Chrome()
  driver.get('%s/static/ark' % (url))
  return driver

# 选择语言, 只有在登陆页面才能进行选择语言控制
def selectLang(driver, value):
  # TODO: 日志纪录
  # TODO: 操作之前需要等待页面加载完成
  # TODO: 操作结束后检查此步操作是否正常/通过页面数据
  # 使用 driver.implicitly_wait 轮询做查询
  driver.find_elements_by_css_selector(".ui-changeLang .el-input")[0].click()
  selectItems = driver.find_elements_by_css_selector(".el-select-dropdown .el-select-dropdown__item")

  driver.implicitly_wait(0.5)

  for item in selectItems:
    if item.text == value:
      item.click()
      break
  return driver

# 启动测试地址
testDriver = startChrome('http://172.16.43.214/')

# 选择中文
selectLang(testDriver, 'English')
