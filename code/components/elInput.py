# 该文件函数用来操作 element-ui 中的 input 组件
import asyncio


class Elinput:
    # @parem driver 浏览器实例
    # @parem selectClassName 选择器类名
    def __init__(self, driver, selectClassName):
        self.element = None
        self.driver = driver
        self.selectClassName = selectClassName
        self.retrieve()

    # 该函数能够重新获取一次页面中的元素
    def retrieve(self):
        element = self.driver.find_elements_by_css_selector('.el-input.%s .el-input__inner' % self.selectClassName)
        if element:
            self.element = element[0]

    # 该函数能够模拟输入框的输入, 第三个参数如果传入True, 将模拟手动打字效果
    async def setValue(self, value, isGradually):
        if isGradually:
            for textItem in list(value):
                self.element.send_keys(textItem)
                await asyncio.sleep(0.1)
        else:
            self.element.send_keys(value)
            await asyncio.sleep(0.1)

    # 清空文本框内容
    async def clear(self):
        self.element.clear()
        await asyncio.sleep(0.1)
