from steps.main import Steps
from base.ChangeLang import ChangeLang



# 创建一个任务流程
step = Steps(ChangeLang('中文'), ...)
# 开始这个任务流程
step.start()
