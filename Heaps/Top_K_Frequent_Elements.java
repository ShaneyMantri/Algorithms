/*
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]

Note:

    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
    It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
    You can return the answer in any order.
*/

import java.util.*;  
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        int res[] = new int[k];
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i : nums) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i)+1);
            } else {
                map.put(i, 1);
            }
        }
        
        PriorityQueue <Integer> heap = new PriorityQueue<>((a,b) -> map.get(b) - map.get(a));
        
        heap.addAll(map.keySet());
        int j = 0;
        while (!heap.isEmpty()) {
            res[j++]=heap.poll();
            if (j==k) {
                return res;
            }
        }
        return res;
    }
}
