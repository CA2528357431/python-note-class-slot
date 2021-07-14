# 多继承中的super

class an:
    def __init__(self):
        self.z=1


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


so=son(3,5,7,9)
print(so.a)

# super有多种可能？
# 出现菱形继承？
# 不用super