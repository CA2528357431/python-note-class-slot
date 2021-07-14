# property


# property可以简化代码

class gtx:
    def __init__(self, core):
        self._deep_core = core

    def set(self, core):
        self._deep_core = core

    @property
    def cache(self):
        cache = self._deep_core / 512
        return cache

    @property
    def processor(self):
        processor = self._deep_core / 4
        return processor


cr = gtx(16)
print(cr.processor)
cr.set(32)
print(cr.processor)

# 与直接定义属性相比，property定义下的’属性‘是动态的，
# 每次调用的时候独立计算，随着因变量而自动改变
