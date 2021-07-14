# property 属性

class rtx:
    def __init__(self,num):
        self._product = num

    def pro1(self):
        return self._product * 2
    # def pro1(self):
    #     return self._product
    # 一般这么写符合逻辑

    def pro2(self, num ):
        self._product = num * 2
    # def pro2(self, num ):
    #     self._product = num
    # 一般这么写符合逻辑

    def pro3(self):
        self._product = 0
        print('delete')

    doc='this is the best card ever'

    product = property(pro1, pro2, pro3, doc)


#
#

# property有四个参数，前三个都是函数，最后一个是该变量的doc
# 1 每当调用 对象.product 其实调用了第一个参数（pro1）
#   创建一个只能从实例调用的类属性，该属性只读
# 2 每当调用 对象.product=某某+某某 其实调用了第二个参数
#   所以可能会有 刚刚card.product=100 结果再看的时候值不为100
#   此时应该看看pro2
#   此后方法一的值也变
# 3 每当调用 del 对象.product 其实调用了第三个参数
# 4 每当调用 对象.product.__doc__,其实调用了第四个参数

if __name__ == '__main__':
    card1 = rtx(1024)
    print(card1.product)

    print()

    card1.product = 1000 - 200
    print(card1.product)
    # 以（1000-200）为参数

    print()

    del card1.product
    print(card1.product)

    print()

    print(rtx.product.__doc__)


# 为什么第二个输出是3200
# card1.product = 1000 - 200 将值设置为1600
# 调用product时返回的是product*2