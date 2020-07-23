# 每个步骤实例放在/base中, 基于TestBase实例
# 每个步骤组放在/steps中, 步骤组相当于几个步骤的组装
# 步骤实例只关注某个步骤的实现与判断
# 步骤组只关注一组步骤的运行

import driver
from steps.login import loginStep

# 启动一个登陆测试
loginDriver = driver.startChrome('http://172.16.43.214/static/ark')

# 启动登录页流程测试
loginStep.run(loginDriver)
