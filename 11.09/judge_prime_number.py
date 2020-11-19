# -*-coding:UTF-8-*-

# Filename:judge_prime_number
# author by:GaoZiqiang

'''
Python 程序用于检测用户输入的数字是否为质数
'''

def judge_prime_number(num):
    # 质数大于1
    if num > 1:
        # 查看因子
        for i in range(2,num):
            if(num%i) == 0:
                print(num,'不是质数')
                print('因为',i,'乘以',num//i,'是',num)
                print('换言之，',num,'有一个非1因子：',i)
                # 这里有一个问题：这里的break的作用域是什么？
                break# 退出循环判断的过程
        else:
            print(num,'是质数')

    else:
        print(num,'不是质数')


def main():
    num = int(input('输入一个数字：'))
    judge_prime_number(num)


if __name__ == '__main__':
    main()