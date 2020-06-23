/*
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

*/

class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int res;
        int n = nums.length;
        int l,e;
        Arrays.sort(nums);
        int sum = nums[0]+nums[1]+nums[2];
        int min = sum;
        for(int i = 0; i<n-2;i++){
            l = i+1;
            e = n-1;
            while(l<e){
                sum = nums[i]+nums[l]+nums[e];
                if(sum==target)
                    return target;
                if (Math.abs(sum-target)<Math.abs(min-target))
                    min=sum;
                else if(sum<target)
                    l++;
                else
                    e--;
            }
        }
        return min;
    }
}
