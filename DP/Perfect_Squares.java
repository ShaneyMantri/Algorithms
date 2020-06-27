/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
*/

import java.lang.Math; 
class Solution {
    public int numSquares(int n) {
        if((int)Math.sqrt(n)==Math.sqrt(n))
            return 1;
        int k= 1;
        int c = 0;
        while (k*k<n){
            c++;
            k++;
        }
        int[][] dp = new int[c+1][n+1];
        for(int i=1;i<(n+1);i++)
        {
            dp[1][i]=i;
        }
        for(int i=2;i<(c+1);i++){
            for(int j=1;j<(n+1);j++){
                if((j-i*i)<0){
                    dp[i][j]=dp[i-1][j];
                }
                else{
                    dp[i][j]=Math.min(dp[i][j-i*i]+1, dp[i-1][j]);
                }
            }
        }
        return dp[c][n];
    }
}
