# doc

class apex:

    '''a game for free and freedom'''

    def __init__(self,na):
        self.age=na

    def show(self):

        '''to show age'''

        print(self.age)

# doc 应当是整体的第一个数据，用‘’‘ ’‘’包裹

print(apex.__doc__)
print(apex.show.__doc__)
# 1 无需实例化
# 2 调用方法的doc时无需加方法的（）

x=apex(1)
print(x.__doc__)
print(x.show.__doc__)
# 实例化也可