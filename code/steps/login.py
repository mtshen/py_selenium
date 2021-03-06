# 登陆页面测试
# 1. 测试选取语言是否正常, 选取英文, 检查登陆按钮的文本是否正常
# 2. 登陆, 登陆一个错误的用户, 检查页面是否弹出错误提示, 检查页面是否跳转
# 3. 登陆, 登陆一个正确的用户, 检查页面是否正常跳转

from steps.main import Steps
from base.view.login import ChangeLang, LoginForm, LoginSubmit

# 载入切换语言任务
stakChLan = ChangeLang('English')
# 载入登陆表单任务
stakLoginForm = LoginForm('admin', '1111111')
# 载入登陆按钮
stakSubmitBtn = LoginSubmit()

# 创建一个步骤组
step = Steps([stakChLan, stakLoginForm, stakSubmitBtn], 'test - 01')


async def startLoginStep(loginDriver):
    await step.start(loginDriver)
