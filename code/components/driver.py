# 载入 webdriver
from selenium import webdriver


# 启动 一个chrome测试页面, 只需要传入IP地址
def startChrome(ip):
    driver = webdriver.Chrome()
    driver.get('http://%s/static/ark' % ip)
    return driver
