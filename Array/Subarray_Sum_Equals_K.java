/*
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
*/


// Method 1
class Solution {
    public int subarraySum(int[] nums, int k) {
        int c = 0;
        int n = nums.length;
        for(int i=1;i<n;i++){
            nums[i]+=nums[i-1];
        }
        
        for(int i=0;i<n-1;i++){
            if(nums[i]==k)
                c++;
            for(int j=i+1;j<n;j++){
                if((nums[j]-nums[i])==k)
                    c++;
            }
        }
        if(nums[n-1]==k)
            return ++c;
        return c;
    }
}


// Method 2
class Solution {
    public int subarraySum(int[] nums, int k) {
        int c = 0;
        int n = nums.length;
        for(int i=0;i<n-1;i++){
            int s = nums[i];
            if(s==k)
                ++c;
            for(int j=i+1;j<n;j++){
                s+=nums[j];
                if(s==k)
                    ++c;
            }
        }
        if(nums[n-1]==k)
            return ++c;
        return c;
    }
}
