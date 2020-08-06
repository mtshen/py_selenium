#### 目录说明:
```
base
-- view     所有页面的操作都存放在这里, 每个页面单独存放一个文件
-- TestBase.py    所有基础步骤的父类

componets
-- drvier.py    用来创建浏览器实例
-- elementUi.py 用来操作ElementUi前端框架下的组件
-- event.py     用来绑定和触发事件
-- journal.py   日志系统

log 所有的日志文件都存储在这里

steps   所有的测试步骤组(用例)都在这里
-- main.py     生成步骤组所依赖的实例

main.py     测试入口
py.test.py  测试文件
README.md   代码的一些说明
```

