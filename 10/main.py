# module 与 class


from backup import *

print('obj ', bate.__module__)
print('obj属性  ', bate.show.__module__)
# 获取对象，或者对象属性所在模块
# 无需实例化
b = bate(1)
print('实例obj ', b.__module__)
print('实例obj属性  ', b.show.__module__)
# 实例化也可

print('-'*50)

print(b.__class__)
# 获取类实例所在的类