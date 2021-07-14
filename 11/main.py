# new 与 init

# 简单来讲，new负责创建对象并分配内存，init负责对对象进行初始化

# 让我们利用new重写做一个单例
#（在基础篇中提过！！）
# （其实装饰器也可以）

class a:
    att=None
    def __init__(self, num):
        self.age = num
    def __new__(cls, *args, **kwargs):
        ip = super().__new__(cls)
        if a.att:
            return a.att
        else:
            a.att = ip
            return a.att


x = a(1)
y = a(2)
print(x.age)