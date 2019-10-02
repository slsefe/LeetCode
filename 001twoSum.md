## 题目描述
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。


## Solution

### 1. 暴力两层循环

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```
时间复杂度O(N^2), 附加空间复杂度O(1), 运行时间6208ms, 内存消耗13.7MB.

### 2. 两次哈希

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()
        for i, item in enumerate(nums):
            d[item] = i
        for i in range(len(nums)):
            tmp = target - nums[i]
            if tmp in d and d[tmp] != i:
                return [i, d[tmp]]
```
时间复杂度O(N), 附加空间复杂度O(N), 运行时间48ms, 内存消耗14.9MB.

### 3. 一次哈希

```
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = dict()
        for i, item in enumerate(nums):
            tmp = target - item
            if tmp in d:
                return [i, d[tmp]]
            d[item] = i
```
时间复杂度O(N), 附加空间复杂度O(N), 运行时间84ms, 内存消耗14.2MB.