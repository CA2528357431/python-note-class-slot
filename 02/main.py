# slot

# 限制只能有slot中的实例属性

class hk:
    __slots__ = ('x','y')
    zz=1
    def __init__(self):
        self.x=1
        self.y=2
        try:
            self.z=1
        except Exception as x:
            print('cannot create')
            print( x)
mac=hk()
print(hk.zz)