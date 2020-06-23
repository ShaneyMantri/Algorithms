/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

*/

import java.lang.*;
import java.util.*;
class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int res = 10000000;
        int n  = nums.length;
        int sum = 0;
        for(int i =0; i<n-2; i++){
            for(int j =i+1; j<n-1; j++){
                for(int k = j+1; k<n;k++){
                    sum = nums[i]+nums[j]+nums[k];
                    if(Math.abs(sum-target)<Math.abs(res-target))
                    {
                        res=sum;
                    }
                }
            }
        }
        return res;
        
        
        
    }
}
