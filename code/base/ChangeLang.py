# 选择语言, 只有在登陆页面才能进行选择语言控制
# 选择元素的 className 为 t_cl_select
# def selectLang(driver, value):
#   # TODO: 日志纪录
#   # TODO: 操作之前需要等待页面加载完成
#   # TODO: 操作结束后检查此步操作是否正常/通过页面数据
#   # 使用 driver.implicitly_wait 轮询做查询

# import re
import asyncio
from base.TestBase import TestBase
from components.elSelect import Elselect


class ChangeLang(TestBase):
    def __init__(self, changeLangName):
        super().__init__('切换语言')
        self.changeLangName = changeLangName

    async def waitReady(self):
        # cUrl = self.driver.current_url
        # matchObj = re.match('static/auth-manage/#/login', cUrl)
        # if cUrl ==

        # 只能在登陆页面进行该步骤
        # self.appointUrl = 'static/auth-manage/#/login'
        # 先等待3秒
        await asyncio.sleep(3)
        return True

    async def run(self):
        langSelectElement = Elselect(self.driver, 't_cl_select')
        await langSelectElement.selectValue(self.changeLangName)

        return True
