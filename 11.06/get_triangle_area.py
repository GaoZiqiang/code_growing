# -*-coding:UTF-8-*-

# FileName:计算三角形面积
# author by:GaoZiqiang

def get_triangle_area(a,b,c):
    # 计算半周长
    s = (a + b + c )/2

    # 计算面积
    area = (s*(s-a)*(s-b)*(s-c))**0.5

    return area

def main():
    # 获取输入
    a = float(input('输入三角形第一条边长：'))
    b = float(input('输入三角形第二条边长：'))
    c = float(input('输入三角形第三条边长：'))

    # get_triangle_area(a,b,c)

    print('经计算三角形面积为：%0.3f'%(get_triangle_area(a,b,c)))


if __name__ == '__main__':
    main()