# -*-coding:UTF-8-*-

# Filename:prime_nnumbers_in_section
# author by:GaoZiqiang

'''
判断并输出指定区间内的所有质数
'''

def judge_output_prime(lower,upper):

    for num in range(lower,upper+1):#range(a,b)取前不取后，所以应该用upper+1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                # 是质数
                print(num)

def main():
    lower = int(input('输入区间下限:'))
    upper = int(input('输入区间上限:'))

    judge_output_prime(lower,upper)

if __name__ == '__main__':
    main()
