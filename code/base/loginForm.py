# 登陆相关表单
import asyncio
from base.TestBase import TestBase
from components.elInput import Elinput


class loginForm(TestBase):
    def __init__(self, userName, passWorld):
        super().__init__('登陆表单')
        self.userNameVal = userName
        self.passworldVal = passWorld

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
        userNameElement = Elinput(self.driver, 't_userName')
        passworldElement = Elinput(self.driver, 't_password')
        await userNameElement.setValue(self.userNameVal, True)
        await passworldElement.setValue(self.passworldVal, True)
        return True
