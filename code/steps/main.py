# main.py 控制一组步骤的执行
# 目前的执行流程是
#   1. checkStepWaitReady 先检查 当前步骤 是否可以触发, 利用步骤中封装的 waitReady 函数
#   2. __start 如果检查通过, 则开始执行 当前步骤, 利用步骤中封装的 run 函数
#   3. __start 等待执行完成, 并检查当前的执行是否生效, 利用步骤中封装的 checkRun 函数
#   4. __start 如果执行成功, 则进入下一个步骤, 重复 流程 1 - 5
#   5. __start 如果执行失败, 终止当前流程组, 直接纪录失败


# TODO: 任务组 Steps 继承自 Event, 因此可以为流程添加自己一些事件的监听

import time
import asyncio
from components.event import Event
from components.journal import Journal

class Steps(Event):
    def __init__(self, steps, name):
        super().__init__()
        # 步骤组名称
        self.name = name
        # 测试步骤
        self.stepList = steps
        # 当前执行到的测试步骤
        self.stepIndex = -1
        # 当前执行的测试步骤实例
        self.step = None
        self.driver = None
        # 步骤是否成功
        self.isDone = False
        # 开始时间
        self.startTime = None
        # 结束时间
        self.endTime = None
        # 失败原因
        self.failLog = ''
        # 载入日志
        self.journal = Journal(self)

    # 启动测试
    async def start(self, driver):
        self.startTime = time.time()

        if driver is None:
            return self.fail("未找到可用的浏览器实例, 检查为步骤组传入的 driver 是否正确!")

        self.driver = driver

        stepLen = len(self.stepList) - 1
        curStepIndex = self.stepIndex
        isSuccess = True

        # 循环执行所有的步骤, 直到某步骤失败或者全部执行完成
        while curStepIndex < stepLen and isSuccess:
            curStepIndex = curStepIndex + 1
            isSuccess = await self.__start()
            # 设置结束时间
            self.step.endTime = time.time()
            # 结算执行完成的步骤
            self.journal.settleStep(self.step)

        # 所有步骤全部执行完成
        if isSuccess:
            return self.success()
        else:
            # 具体失败原因在 __start() 中结算
            return False

    async def __start(self):
        stepIndex = self.stepIndex + 1
        self.stepIndex = stepIndex

        curStep = self.stepList[stepIndex]
        self.step = curStep
        # 设置开始时间
        curStep.startTime = time.time()
        # 设置当前步骤顺序
        curStep.index = stepIndex + 1
        # 绑定浏览器实例
        curStep.setDriver(self.driver)

        # 等待事件成立
        isReady = await self.checkStepWaitReady()

        if isReady:
            # 如果条件成立则开始走测试
            await curStep.run()
            # 测试执行结束, 开始检查测试是否成功
            isCheckRun = await curStep.checkRun()

            # 执行成功与失败
            if isCheckRun:
                # 成功, 标记成功
                curStep.isDone = True
                await curStep.success()
                return True
            else:
                # 失败, 标记失败
                curStep.isDone = False
                await curStep.fail()
                return self.fail("执行步骤 [%s] 失败" % curStep.name)

        else:
            # 失败, 标记失败
            curStep.isDone = False
            await curStep.fail()
            # 失败结果在 checkStepWaitReady 中结算
            return False

    # 检查 当前步骤 是否可以进行
    async def checkStepWaitReady(self):
        if self.step is not None:
            curStep = self.step
            curStepReadyTimeNumber = curStep.readyTimeNumber
            curStepReadyTimeClockInterval = curStep.readyTimeClockInterval

            # 执行前对参数进行检查
            if curStepReadyTimeNumber < 0 or curStepReadyTimeClockInterval < 0:
                # 如果参数不合法
                return self.fail("步骤 [%s] 设置的检查时间参数不合法" % curStep.name)

            # 开始等待条件判断的成立与失败
            while True:
                # 等待条件判断
                isReady = await curStep.waitReady()

                # 如果条件成立 退出循环 直接返回True
                if isReady:
                    return True

                # 等待
                await asyncio.sleep(curStepReadyTimeClockInterval)

                # 等待时间如果消耗完则直接返回失败
                curStepReadyTimeNumber = curStepReadyTimeNumber - curStepReadyTimeClockInterval
                if curStepReadyTimeNumber < 0:

                    # 标记超时
                    curStep.isOvertime = True
                    return self.fail("步骤 [%s] 等待超时" % curStep.name)

        else:
            # 走到这里说明程序出错了
            return self.fail("未找到可用的步骤实例")

    def fail(self, failLog):
        self.isDone = False
        self.failLog = failLog
        self.endTime = time.time()
        self.journal.settleSteps()
        return False

    def success(self):
        self.isDone = True
        self.endTime = time.time()
        self.journal.settleSteps()
        return True
