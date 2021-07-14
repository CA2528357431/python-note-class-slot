# str 与 dict

class sth:

    pub = 'hello'

    def __init__(self,num):
        self.age=num
        self.lover='wyx'

    def __str__(self):

        string='my age is ' + str(self.age)
        return string

    # 当print实例对象的时候输出的内容

peo = sth(9)
print(peo)


dic=peo.__dict__
print(type(dic))
print(dic)

# 字典形式的实例对象所有的属性
