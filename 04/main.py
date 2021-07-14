# MRO 与 super



class an:
    def __init__(self):
        print("don't touch me")


class fa(an):
    def __init__(self, a, b):
        an.__init__(self)
        self.a = a
        self.b = b


class mo(an):
    def __init__(self, c, d):
        an.__init__(self)
        self.c = c
        self.d = d


class son(fa, mo):
    def __init__(self, a, b, c, d):
        fa.__init__(self, a, b)
        mo.__init__(self, c, d)


a = son(1,2,3,4)
print(a.a)
print(a.b)
print(a.c)
print(a.d)
# 发现需要多次调用an构造,浪费资源

print(son.mro())
# 显示mro线性结构，利用他可以使每个类最多调用一次
# super就是按照此顺序向后调用！！！！
# 本例中，fa的super调用mo！！！
# MRO排列原则
# 越低级的元素越靠前
# 同级别元素，越先继承越靠前

class an1:
    def __init__(self):
        print("don't touch me")


class fa1(an1):
    def __init__(self, a, b, c, d):
        super(fa1, self).__init__(c, d)
        self.a = a
        self.b = b


class mo1(an1):
    def __init__(self, c, d):
        super(mo1, self).__init__()
        self.c = c
        self.d = d


class son1(fa1, mo1):
    def __init__(self, a, b, c, d):
        super(son1, self).__init__(a,b,c,d)

b=son1(1,2,3,4)
print(b.a)
print(b.b)
print(b.c)
print(b.d)
