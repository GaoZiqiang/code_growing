num = int(input('输入一个整数:'))
# pwr和root先初始化
if num == 0:
    print('root=',0,'pwr=',0)
else:
    pwr = 1
    root = 0
    while pwr < 6:
        while root*pwr < num:
            root = root + 1
        pwr = pwr + 1

if pwr > 0 and pwr < 6 and root*pwr == num:
    print('success')
else:
    print('failure')
