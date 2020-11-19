# -*-coding_UTF-8-*-

# 计算复数的平方根

# 导入复数数学模块
import cmath

num = float(input('输入一个数字：'))
num_sqrt = cmath.sqrt(num)
if num > 0:
    num_sqrt = num**0.5
    print('{0}的平方根为{1:0.3f}'.format(num,num_sqrt))
else:
    num_sqrt = cmath.sqrt(num)
    print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
