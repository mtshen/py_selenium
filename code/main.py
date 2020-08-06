# 步骤: 测试用的最小单元, 表示某一个动作, 如 选择下拉框, 输入一个表单 等...
# 所有的步骤都存放在 base 目录中
# 步骤组: 拼接多个步骤成为步骤组, 可对应一个测试用例
# 步骤组 主要依赖于 steps/main.py 文件, 所有的步骤组都存放在 steps 目录中

# components 中存储了一些常用的包

# 依赖外部包 asyncio, selenium

import asyncio
from components import driver
from steps.login import startLoginStep

# 创建异步实例
loop = asyncio.get_event_loop()

# 启动一个登陆测试, 可以创建多个实例进行多个步骤组同步进行测试
loginDriver = driver.startChrome('172.16.43.214')
# loginDriver = driver.startChrome('localhost:8080')

# 网页最大化
loginDriver.maximize_window()

# 启动登录页流程测试, asyncio.wait 中传入是一个数组, 要同步执行的步骤组
loop.run_until_complete(asyncio.wait([
  startLoginStep(loginDriver)
]))

# 完成后关闭异步实例
loop.close()
