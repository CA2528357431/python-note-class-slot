# property

class rtx:
    def __init__(self, core):
        self._deep_core = core

    @property
    def core(self):
        return self._deep_core

    @core.setter
    def core(self, value):
        self._deep_core = value

    @core.deleter
    def core(self):
        del self._deep_core
        print('delete _deep_core')


# 有安全需要的数据应该用property

# 调用property函数无需添加（）
# 使get函数变成一个只读变量
card = rtx(100)
print(card.core)

# @方法.setter 使对这个只读变量可修改,
# 而且对应的原变量也随之改变
card.core = 30
print(card.core)

# @方法.deleter 使对这个只读变量删除,
# 而且对应的动态变量也随之删除
del card.core
try:
    print(card.core)
except:
    print('no such core')
