"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

It doesn't matter what values are set beyond the returned length.


"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 1
        i = 1
        j = 1
        n=len(nums)
        l = 1
        if len(nums)<=2:
            return len(nums)
        while j<n:
            if nums[j]==nums[j-1]:
                if count<2:
                    nums[i]=nums[j]
                    j+=1
                    i+=1
                    count+=1
                    l+=1
                elif count==2:
                    j+=1
            else:
                count=1
                nums[i]=nums[j]
                j+=1
                i+=1
                l+=1
        return l
                
