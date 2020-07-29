from asyncio import asyncio
from components.event import Event

class Steps(Event):
  def __init__(self, **steps):
    super().__init__()

    # 测试步骤
    self.stepList = steps
    # 当前执行到的测试步骤
    self.stepIndex = -1
    # 当前执行的测试步骤实例
    self.step = None
    self.driver = None

  # 启动测试
  async def start(self, driver):
    if driver == None:
      print("未找到 driver!")
      return False

    self.driver = driver

    print("准备开始一个测试步骤组, 准备变量")
    stepLen = len(self.stepList) - 1
    curStepIndex = self.stepIndex
    isSuccess = True


    print("开始执行")
    # 循环执行所有的步骤, 直到某步骤失败或者全部执行完成
    while curStepIndex < stepLen and isSuccess == True:
      curStepIndex = curStepIndex + 1
      isSuccess = await self.__start()

  async def __start(self):
    stepIndex = self.stepIndex + 1
    self.stepIndex = stepIndex
    print("执行第" + str(stepIndex + 1) + "个...")

    curStep = self.stepList[stepIndex]
    self.step = curStep

    # 等待事件成立
    isReady = await self.checkStepWaitReady()

    if isReady:
      # 如果条件成立则开始走测试
      await curStep.run()
      # 测试执行结束, 开始检查测试是否成功
      isCheckRun = await curStep.checkRun()

      # 执行成功与失败
      if isCheckRun:
        await curStep.success()
        return True
      else:
        await curStep.fail()
        return False

    else
      # 失败
      await curStep.fail()
      return False

  async def checkStepWaitReady(self):
    if self.step != None:
      curStep = self.step
      curStepReadyTimeNumber = curStep.readyTimeNumber
      curStepReadyTimeClockInterval = curStep.readyTimeClockInterval

      # 执行前对参数进行检查
      if curStepReadyTimeNumber < 0 or curStepReadyTimeClockInterval < 0:
        # 如果参数不合法
        print("当前步骤设置的时间参数不合法")
        return False


      # 开始等待条件判断的成立与失败
      while True:
        # 等待条件判断
        isReady = await curStep.waitReady()

        # 如果条件成立 退出循环 直接返回True
        if isReady == True:
          return True

        # 等待
        await asyncio.sleep(curStepReadyTimeClockInterval)

        # 等待时间如果消耗完则直接返回失败
        curStepReadyTimeNumber = curStepReadyTimeNumber - curStepReadyTimeClockInterval
        if curStepReadyTimeNumber < 0:
          return False

    else:
      # 走到这里说明程序出错了!
      print('未找到可用的步骤实例!')
      return False


