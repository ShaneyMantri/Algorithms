"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = [0]*(len(nums1)+len(nums2))
        i = 0
        j=0
        k = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                n[k]=nums1[i]
                i+=1
                k+=1
            else:
                n[k]=nums2[j]
                j+=1
                k+=1
                
        if i<len(nums1):
            while i<len(nums1):
                n[k]=nums1[i]
                i+=1
                k+=1
        elif j<len(nums2):
            while j<len(nums2):
                n[k]=nums2[j]
                k+=1
                j+=1
                
        if len(n)%2==0:
            med = (n[len(n)//2]+n[len(n)//2 - 1])/2
            return med
        else:
            return n[len(n)//2]
            
        
