# -*- coding: UTF-8 -*-

# Filename:is_number
# author by:GaoZiqiang

# 注意：是测试数字，因此输入字符应该是unicode编码中的数字，也就是各种语言中表示数字的字符，比如中文的数字2为“二”，泰语中的数字2为“๒”
from IPython import embed

def is_number(s):
    # 第一个是狭义上的阿拉伯数字
    try:
        float(s)
        return True# 如果没有报错就返回True
    except ValueError:# 否则（出现了ValueError）就进入下一个try判断
        pass
    # 第二个是广义上的unicode编码中的数字
    try:
        import unicodedata
        unicodedata.numeric(s)# 如果没有报错就返回True；unicodedata.numeric(s)返回分配给字符s的数字值
        return True
    except (TypeError, ValueError):# 出现了TypeError或ValueError
        pass

    return False


embed()

# 测试字符串和数字
print(is_number('foo'))   # False
# embed()
print(is_number('1'))     # True
print(is_number('1.3'))   # True
print(is_number('-1.37')) # True
print(is_number('1e3'))   # True

# 测试 Unicode
# 阿拉伯语 5
print(is_number('٥'))  # True
# 泰语 2
print(is_number('๒'))  # True
# 中文数字
print(is_number('四')) # True
# 版权号
print(is_number('©'))  # False