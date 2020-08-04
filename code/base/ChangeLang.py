# 选择语言, 只有在登陆页面才能进行选择语言控制
# def selectLang(driver, value):
#   # TODO: 日志纪录
#   # TODO: 操作之前需要等待页面加载完成
#   # TODO: 操作结束后检查此步操作是否正常/通过页面数据
#   # 使用 driver.implicitly_wait 轮询做查询

import asyncio
from typing import re
from base.TestBase import TestBase


class ChangeLang(TestBase):
    def __init__(self, changeLangName):
        super().__init__('切换语言')
        self.changeLangName = changeLangName

    async def waitReady(self):
        cUrl = self.driver.current_url
        matchObj = re.match('static/auth-manage/#/login', cUrl)
        if cUrl ==
        #
        # 只能在登陆页面进行该步骤
        # self.appointUrl = 'static/auth-manage/#/login'
        # 先等待3秒
        await asyncio.sleep(3)
        return True

    async def run(self):
        driver = self.driver
        changeLangName = self.changeLangName

        driver.find_elements_by_css_selector(".ui-changeLang .el-input")[0].click()
        selectItems = driver.find_elements_by_css_selector(".el-select-dropdown .el-select-dropdown__item")

        await asyncio.sleep(0.5)

        for item in selectItems:
            if item.text == changeLangName:
                item.click()
                break

        return True
