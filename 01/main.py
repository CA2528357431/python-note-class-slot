class hk:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c


    #property
    #暗示标量不建议直接访问而要用函数访问
    @property
    def get_a(self):
        return self.a