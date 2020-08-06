# 日志系统
import os
import time
import random

# 步骤组模板
stepsTemplate = """
步骤组: {name}
开始时间: {startTime}

----------------------------------------------
{stepLog}

步骤结束
{errorLog}
结束时间: {endTime}
总耗时: {time}ms
"""

# 步骤模板
# TODO: 步骤组带s, 步骤不带s
stepTemplate = """
步骤{index}: {name}
{runLog}
结果: {result}
开始时间: {startTime}
结束时间: {endTime}
耗时: {time}ms
----------------------------------------------
"""


def createLog(name, log):
    # 创建当前日期文件名
    curDate = time.strftime("%Y%m%d", time.localtime())
    curPath = os.getcwd() + '/log/' + curDate
    logFilePath = curPath + '/' + name + '.log'
    isExist = os.path.exists(curPath)
    if not isExist:
        os.makedirs(curPath)

    file = open(logFilePath, 'w')
    file.write(log)
    file.close()
    return logFilePath


class Journal:
    def __init__(self, steps):
        # 步骤组数据
        self.steps = steps
        self.log = ''
        self.contentLog = [{} for i in range(len(steps.stepList))]

    # 结算步骤
    def settleStep(self, step):
        name = step.name
        index = step.index
        runLog = step.getLogText()
        startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(step.startTime))
        endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(step.endTime))
        timeConsum = round(step.endTime - step.startTime, 2)
        if step.isDone:
            result = '成功'
        elif step.isOvertime:
            result = '等待超时, 失败'
        else:
            result = '失败'

        logItem = stepTemplate.format(
            index=index, name=name, runLog=runLog, result=result,
            startTime=startTime, endTime=endTime, time=timeConsum,
        )

        self.contentLog[index - 1] = logItem

    # 结算步骤组
    def settleSteps(self):
        name = self.steps.name
        stepLog = ''.join(self.contentLog)
        startTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.steps.startTime))
        endTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.steps.endTime))
        timeConsum = round(self.steps.endTime - self.steps.startTime, 2)
        errorLog = self.steps.failLog

        self.log = stepsTemplate.format(
            name=name, stepLog=stepLog, startTime=startTime, endTime=endTime, time=timeConsum, errorLog=errorLog
        )

        print(self.log)
        createLog(name + str(random.randint(10000, 99999)), self.log)
