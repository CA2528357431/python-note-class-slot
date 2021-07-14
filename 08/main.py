# __call__方法

class bate:
    def __init__(self, a, b, c):
        self.id = a
        self.age = b
        self.hope = c

    def show(self):
        print('id: ',self.id)
        print('age: ', self.age)
        print('hope: ', self.hope)

    def __call__(self):
        print('cooooooooooool')
    #__call__函数在 对象() 结构出现时被调用

ex=bate(5,9,1)
ex()