num = int(input('输入一个整数:'))
# pwr和root先初始化
if num == 0:
    print('root=',0,'pwr=',0)
else:
    pwr = 1
    root = 0
    while pwr < 6:
        while root*pwr < num:
            root = root + 1# 当root*pwr的条件满足时外层while并不能及时退出，会造成一些浪费
        if pwr > 0 and pwr < 6 and root*pwr == num:
            print('root=',root,'pwr=',pwr)
            print('success')
            break
        else:
            print('root=',root,'pwr=',pwr)
            print('failure')
            break

        pwr = pwr + 1
