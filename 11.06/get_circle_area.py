# -*-coding:UTF-8-*-

# FileName:get_circle_area
# author by:GaoZiqiang
PI = 3.142

def get_circle_area(r):

    return PI*r**2

def main():
    # 获取半径
    r = float(input('输入半径：'))

    print('圆的面积为：%0.3f'%(get_circle_area(r)))


if __name__ == '__main__':
    main()