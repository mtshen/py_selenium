# 载入selenium
from selenium import webdriver

# 启动 一个chrome测试页面
def startChrome(url):
  driver = webdriver.Chrome()
  driver.get('%s/static/ark' % (url))
  return driver