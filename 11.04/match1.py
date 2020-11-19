#!/usr/bin/python

# re.match函数默认从字符串的开头处开始匹配。与search函数相对应，search函数可以从字符串的任意位置进行匹配
# 如果字符串开始不符合正则表达式，则匹配失败，函数返回None
import re
print(re.match('www', 'www.nowcoder.com').span())  # 在起始位置匹配
print(re.match('com', 'www.nowcoder.com'))         # 不在起始位置匹配
