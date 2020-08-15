"""
There are N dominoes in a line, and we place each domino vertically upright.

In the beginning, we simultaneously push some of the dominoes either to the left or to the right.



After each second, each domino that is falling to the left pushes the adjacent domino on the left.

Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

Given a string "S" representing the initial state. S[i] = 'L', if the i-th domino has been pushed to the left; S[i] = 'R', if the i-th domino has been pushed to the right; S[i] = '.', if the i-th domino has not been pushed.

Return a string representing the final state. 

Example 1:

Input: ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
Example 2:

Input: "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
"""
## METHOD 1 Brute Force AC 

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        flag = 0
        n = len(dominoes)
        if n==0 or n==1:
            return dominoes
        st = list(dominoes)
        while True:
            flag=0
            d = st.copy()
            for i in range(n):
                if st[i]=="R":
                    if i==n-2 and st[i+1]==".":
                        d[i+1]="R"
                        flag=1
                        
                    if i<n-2:
                        if st[i+1]=="." and st[i+2]!="L":
                            d[i+1]="R"
                            flag=1
                                            
                elif st[i]=="L":
                    if i>=1:
                        if i==1:
                            if st[i-1]==".":
                                d[i-1]="L"
                                flag=1
                        else:
                            if st[i-1]=="." and st[i-2]!="R":
                                d[i-1]="L"
                                flag=1
            st = d.copy()
            if flag==0:
                return ''.join(st)
                            
                        
                        
