from typing import List
'''
从nums[]数组中找到target的两个加数
leetcode：https://leetcode-cn.com/problems/two-sum/
author by :GaoZiqiang
'''

def twoSum(nums,target):
    # nums = [2, 7, 11, 15]
    # target = 9
    n = len(nums)
    # 若nums数组中元素少于2
    if n < 2:
        return
    else:
        for i in range(n):
            for j in range(i + 1, n):# i+1：下一个元素
                if nums[i] + nums[j] == target:
                    print(i, j)

def main():
    nums = [2,7,11,15]
    target = 18
    twoSum(nums,target)

if __name__ == '__main__':
    main()
