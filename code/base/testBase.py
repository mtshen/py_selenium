# 每个测试步骤为一个 TestBase
# 每个测试步骤完整的包括
# 1. 操作之前需要加载条件的成立, 如指定网页的加载完成, 某元素的出现等
# 2. 执行测试步骤, 每一步需要模拟手工点击, 至少等待0.1秒
# 3. 执行测试步骤结束后需要检查操作是否正常/通过页面数据等手段
# 期间测试日志需要及时记录

class TestBase:
  # 初始化实例属性
  def __init__(self, testName):
    super().__init__()

    # 测试步骤名称, 用于纪录日志
    self.name = testName
    # 加载条件成立最长等待时间, 超时按失败处理, 默认5秒, 如果为0 则不设置等待时间
    self.readyTimeNumber = 5
    # 加载条件成立检查间隔, 默认100ms
    self.readyTimeClockInterval = 0.1
    # 测试窗口
    self.driver = None

  # 函数有2个参数,调用 resolve 视为成功, 调用 reject 视为失败
  # 本来打算用标准 Promise, 后来换成了 asyncio 提供异步编程

  # 等待条件
  async def waitReady(self):
    return True

  # 执行步骤
  async def run(self):
    return True

  # 结束检查是否成功
  async def checkRun(self):
    return True

  # 成功的回调函数
  async def success(self):
    return

  # 失败的回调函数
  async def fail(self):
    return

  def setDriver(self, driver):
    self.driver = driver
    return
