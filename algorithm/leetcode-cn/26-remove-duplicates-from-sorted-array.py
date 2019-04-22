#!/usr/bin/env python
#coding: utf-8

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p = 0 if nums else -1
        for i in range(1, len(nums)):
            if nums[i] != nums[p]:
                p += 1
                nums[p] = nums[i]
        return p + 1
