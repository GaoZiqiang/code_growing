# -*-coding:UTF-8-*-

# 求解二次方程

import cmath

from IPython import embed

def get_quadratic_equation(a,b,c):
    d = (b**2) - (4*a*c)
    # 下面进行分类型讨论

    if d > 0:
        print('该方程有两个不同的解：')
        print((-b + (d**0.5))/(2*a),(-b - (d**0.5))/(2*a))
    elif d == 0:
        print('该方程只有一个二重解：')
        print((-b + (d**0.5))/(2*a))
    else:
        print('该方程有两个虚根：')
        print('第一个解：{0:0.3f}+{1:0.3f}j'.format((-b)/(2*a),((-d)**0.5)/(2*a)))
        print('第二个解：{0:0.3f}-{1:0.3f}j'.format((-b)/(2*a),((-d)**0.5)/(2*a)))
        # embed()
    # sol1 = (-b + cmath.sqrt(d))/(2*a)
    # sol2 = (-b - cmath.sqrt(d))/(2*a)

    # return sol1,sol2

def main():
    print('构建一元二次方程组')
    a = float(input('输入二次项参数a：'))
    b = float(input('输入一次项参数b：'))
    c = float(input('输入常数项c：'))
    print('得到的方程组为：{0:0.3f}x^2 + {1:0.3f}x + {2:0.3f} = 0'.format(a,b,c))

    print('解方程组得：')
    get_quadratic_equation(a,b,c)
    # print(sol1)
    # print(sol2)

if __name__ == "__main__":
    main()