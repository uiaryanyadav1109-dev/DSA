class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d=dict()
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            need=target-nums[i]
            if (need in d.keys () and d[need] != i):
                return i,d[need]

