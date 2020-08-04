# 事件模块
# 用来绑定或解绑一些事件
# TODO: 可以绑定事件, 但是目前无法触发 events = self.__event[eventName] 无法执行?
class Event:
    def __init__(self):
        super().__init__()
        self.__event = {}

    # 用来绑定事件
    # @param eventName 事件名称
    # @param eventFn 事件
    def on(self, eventName, eventFn):
        if hasattr(self.__event, eventName):
            self.__event[eventName].append(eventFn)
        else:
            self.__event[eventName] = [eventFn]
        return self

    # 用来解绑事件
    def off(self, eventName, eventFn):
        events = self.__event[eventName]
        if events:
            # 如果不传入eventFn则视为全部删除
            if eventFn:
                for index in range(len(events)):
                    eventItem = events[index]
                    if eventItem == eventFn:
                        events.pop(index)
                        break
            else:
                self.__event.pop(eventName)
        return self

    # 用来触发某些事件
    # @param eventName 事件名称
    # @param data 触发该事件时传入的数据
    def trigger(self, eventName, data):
        events = self.__event[eventName]
        for eventItem in events:
            eventItem(data)
        return self
