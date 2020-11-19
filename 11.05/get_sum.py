# -*- coding: UTF-8 -*-

# 使用Python实现数字求和

# 用户输入数字
num1 = input('输入第一个数字：')
num2 = input('输入第二个数字：')

# 求和
sum = float(num1) + float(num2)# input() 返回一个字符串，所以我们需要使用 float() 方法将字符串转换为数字

# 显示计算结果
print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
# 另一种写法
# print('数字 {} 和 {} 相加结果为： {}'.format(num1, num2, sum))


# 代码优化
print('两数之和%.1f'%(float(input('输入第一个数字：')) + float(input('输入第二个数字：'))))

