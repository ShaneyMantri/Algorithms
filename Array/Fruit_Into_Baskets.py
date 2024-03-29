""""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: 
you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?
Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].
Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].
Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].
Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
""""
# AC 860ms

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        d = {}
        first = -1
        second = -1
        i = 0
        n = len(tree)
        m = -1
        while i<n:
            if tree[i] in d:
                d[tree[i]].append(i)
                i+=1
            else:
                if len(d.keys())==2:
                    s = 0
                    for k,v in d.items():
                        s+=len(v)
                    m = max(m, s)
                    if d[first][-1]>d[second][-1]:
                        i = d[second][-1]+1
                        first = first
                        d = {}
                        d[tree[i]] = [i]
                        i+=1
                    else:
                        i = d[first][-1]+1
                        first = second
                        d = {}
                        d[tree[i]] = [i]
                        i+=1
                elif len(d.keys())==1:
                    second = tree[i]
                    d[tree[i]] = [i]
                    i+=1
                else:
                    first = tree[i]
                    d[tree[i]] = [i]
                    i+=1
        s = 0
        for k,v in d.items():
            s+=len(v)
        return max(m, s)
        
