# -*-coding:UTF-8-*-
'''
解法2：
从nums[]数组中找到target的两个加数

leetcode：https://leetcode-cn.com/problems/two-sum/
author by :GaoZiqiang
'''

def twoSum(nums,target):

    hashtable = dict()
    for i, num in enumerate(nums):# i是数组下标号，num是数组中的元素
        if target - num in hashtable:
            print(hashtable[target - num], i)
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []

def main():
    nums = [2,7,11,15]
    target = 9
    twoSum(nums,target)

if __name__ == '__main__':
    main()