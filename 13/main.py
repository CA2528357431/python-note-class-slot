# getitem steitem delitem

class rtx:
    def __init__(self, num):
        self.age = num
        self.dic = {}

    def __setitem__(self, key, value):
        self.dic[key] = value
        print('set %s as %s' % (key, value))

    def __getitem__(self, item):
        print('get %s' % (item,))
        return self.dic[item]

    def __delitem__(self, key):
        del self.dic[key]
        print('del %s' % (key,))

    # 总有蠢货希望以 obj['sth']的形式调用属性
    # 如是的方法为他们提供了便利


card = rtx(10)
card['core'] = 100
print(card['core'])
del card['core']
