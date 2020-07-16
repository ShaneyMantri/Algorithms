"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0:
            return []
        if len(nums)==1:
            return [str(nums[0])]
            
        res = []
        st = 0
        en = 0
        n = len(nums)
        
        while en<(n-1):
            if nums[en]==(nums[en+1]-1):
                en+=1
                
            else:
                if st==en:
                    res.append(str(nums[st]))
                    
                else:
                    res.append(str(nums[st])+"->"+str(nums[en]))
                    
                en+=1
                st = en
                
        if (nums[-1]-1)==nums[-2]:
            res.append(str(nums[st])+"->"+str(nums[-1]))
            
        else:
            res.append(str(nums[-1]))
            
        return res
                
        
