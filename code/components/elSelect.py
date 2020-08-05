# 该文件函数用来操作 element-ui 中的 select 组件
import asyncio


class Elselect:
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
