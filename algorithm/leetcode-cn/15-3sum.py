#!/usr/bin/env python
#coding: utf-8

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        sorted_nums = sorted(nums)
        res = []
        for i in range(length - 2):
            start = i + 1
            end = length - 1
            while start < end:
                if sorted_nums[i] + sorted_nums[start] + sorted_nums[end] == 0:
                    if (sorted_nums[i], sorted_nums[start], sorted_nums[end]) not in res:
                        print sorted_nums[i], sorted_nums[start], sorted_nums[end]
                        res.append((sorted_nums[i], sorted_nums[start], sorted_nums[end]))
                    if sorted_nums[start] == sorted_nums[start+1]:
                        start += 1
                    else:
                        end -= 1
                elif sorted_nums[i] + sorted_nums[start] + sorted_nums[end] > 0:
                    end -= 1
                else:
                    start += 1
        return res

if __name__ == "__main__":
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1, -4])
