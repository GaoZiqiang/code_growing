# 用二分查找法求平方根
x = int(input('输入整数:'))
if x < 0:
    print('该整数{0}没有平方根'.format(x))
else:
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0,x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon and low != high:
        print('low=',low,'high=',high,'ans=',ans)
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (low + high)/2

    print('numGuesses=',numGuesses)
    print(ans,'is close to square root of',x)    

