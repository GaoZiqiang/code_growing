name_handle = open('kids','w')# open()函数是python内置的函数，因此不需要调用第三方库

# 文件写入
for i in range(2):
    name = input('enter name:')
    name_handle.write(name + '\n')
name_handle.close()

name_handle = open('kids','r')
for line in name_handle:
        print(line[:-1])
name_handle.close()
