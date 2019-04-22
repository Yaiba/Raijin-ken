#!/usr/bin/env python
#coding: utf-8

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match_nums = {}
        for i, x in enumerate(nums):
            if x in match_nums:
                return match_nums[x], i
            else:
                match_nums[target - x] = i
