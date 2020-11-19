#!/usr/bin/python3
import re
# 要注意matchObj.group()函数
# group(0)或者默认group()返回匹配的整个字符串
# group(1)、group(2)分别返回匹配的子组
# group(1,2)返回一个元组，包含两个子组

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

if matchObj:
   print ("matchObj.group() : ", matchObj.group())
   print ("matchObj.group(1) : ", matchObj.group(1))
   print ("matchObj.group(2) : ", matchObj.group(2))
else:
   print ("No match!!")
