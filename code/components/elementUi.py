# 该文件函数用来快速操作Element-Ui 前端框架中的组件
import asyncio


class ElInput:
    # input 组件操作
    # @parem driver 浏览器实例
    # @parem inputClassName 选择器类名
    def __init__(self, driver, inputClassName):
        self.element = None
        self.driver = driver
        self.inputClassName = inputClassName
        self.retrieve()

    # 该函数能够重新获取一次页面中的元素
    def retrieve(self):
        element = self.driver.find_elements_by_css_selector('.el-input.%s .el-input__inner' % self.inputClassName)
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


class ElSelect:
    # @parem driver 浏览器实例
    # @parem selectClassName 选择器类名
    def __init__(self, driver, selectClassName):
        self.element = None
        self.driver = driver
        self.selectClassName = selectClassName
        self.retrieve()

    # 该函数能够重新获取一次页面中的元素
    def retrieve(self):
        element = self.driver.find_elements_by_css_selector('.el-select.' + self.selectClassName)
        if element:
            self.element = element[0]

    # 该函数能够触发选择框的点击, 用于呼出下拉框, 内置了0.2秒的延迟, 模拟人手点击的延迟
    async def click(self):
        self.element.click()
        await asyncio.sleep(0.2)

    # 该函数能够选取页面中的指定值
    async def selectValue(self, value):
        await self.click()

        # 选取下拉框
        selectItems = self.driver.find_elements_by_css_selector(
            ".el-select-dropdown.%s_popper .el-select-dropdown__item" % self.selectClassName
        )

        # 寻找指定值并点击
        for item in selectItems:
            if item.text == value:
                item.click()
                break


class ElButton:
    # @parem driver 浏览器实例
    # @parem selectClassName 选择器类名
    def __init__(self, driver, ButtonClassName):
        self.element = None
        self.driver = driver
        self.ButtonClassName = ButtonClassName
        self.retrieve()

    # 该函数能够重新获取一次页面中的元素
    def retrieve(self):
        element = self.driver.find_elements_by_css_selector('.el-button.' + self.ButtonClassName)
        if element:
            self.element = element[0]

    # 该函数能够触发选择框的点击, 用于呼出下拉框, 内置了0.2秒的延迟, 模拟人手点击的延迟
    async def click(self):
        self.element.click()
        await asyncio.sleep(0.2)
