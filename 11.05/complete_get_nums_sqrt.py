# -*-coding_UTF-8-*-

'''
综合各种类型的数字求平方根
函数集成
'''

import cmath

# 正数
def pos_sqrt(num):
    return num**0.5

# 负数
def neg_sqrt(num):
    return cmath.sqrt(num)

# 复数
def complex_sqrt(num_real,num_imag):
    return cmath.sqrt(complex(float(num_real),float(num_imag)))

# 主函数
def main():
    num = float(input('输入一个正数：'))
    print('{0}的平方根为：{1:0.3f}'.format(num,pos_sqrt(num)))

    num = float(input('输入一个负数：'))
    print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num,neg_sqrt(num).real,neg_sqrt(num).imag))

    print('输入一个复数：')
    num_real = float(input('输入实部：'))
    num_imag = float(input('输入虚部：'))
    print('请确认你输入的复数为：{0:0.3f}+{1:0.3f}j'.format(num_real,num_imag))
    # num = float(input('输入一个复数：'))
    print('{0:0.3f}+{1:0.3f}j的平方根为{2:0.3f}+{3:0.3f}j'.format(num_real,num_imag,complex_sqrt(num_real,num_imag).real,complex_sqrt(num_real,num_imag).imag
                                                             ))
if __name__ == "__main__":
    main()