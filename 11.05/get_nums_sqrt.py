#计算输入数字的平方根
import cmath

#输入的数字只能是正数
def sqrt1(number) :
    number_sqrt = number ** 0.5#使用指数运算符 ** 来计算该数的平方根
    return number_sqrt

#输入的数可以是负数
def sqrt2(number) :
    number_sqrt = cmath.sqrt(number)#使用了cmath里面的sqrt方法
    return number_sqrt

#输入的数也可以是复数
def sqrt3(num_real,num_imag) :

    num_sqrt = cmath.sqrt(complex(float(num_real), float(num_imag)))
    return num_sqrt

def main() :
    num = float(input('请输入一个正数：'))
    print('%.3f 的平方根是：%.3f' %(num,sqrt1(num))) #%的数量要和后面的数字个数对应，不然会打印错误
    num1 = int(input('请输入一个负数：'))
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num1 ,sqrt2(num1).real,sqrt2(num1).imag))

    #调用函数时，参数传递一定要正确
    num_real = float(input('请输入实部：'))
    num_imag = float(input('请输入虚部：'))
    print('你输入的复数为：{0:0.3f}+{1:0.3f}j'.format(num_real,num_imag))
    #使用反斜杠完成一个语句多行编写功能
    print('{0}+{1}j的平方根为{2:0.3f}+{3:0.3f}j'.format(num_real, num_imag, \
                                                   sqrt3(num_real,num_imag).real, \
                                                   sqrt3(num_real,num_imag).imag))

if __name__ == "__main__" :
    main()
