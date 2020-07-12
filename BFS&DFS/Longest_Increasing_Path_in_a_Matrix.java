/*
Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
*/


// TLE 137/138
class Solution {
    int res = 0;
    public void dfs(int i ,int j,int[][] mat,int m, int n,int count, int[][] v, int min, int l){
        if (this.res==(m*n)){
                return;
            }
        if (i>=m || i<0)
            return;
        if (j>=n || j<0)
            return ;
        
        if (count>this.res){
            this.res = count;
            if (this.res==(m*n)){
                return;
            }
        }
        if(mat[i][j]==min)
            return;
        if(i>0){
            
            if(v[i-1][j]==0){
                if(mat[i-1][j]<mat[i][j]){
                    v[i-1][j]=l+1;
                    this.dfs(i-1, j, mat, m,n,count+1,v, min,l+1);
                    
                }
            }
            else{
                if(mat[i-1][j]<mat[i][j]){
                    if(v[i-1][j]<(l+1))
                    {
                        v[i-1][j]=l+1;
                    this.dfs(i-1, j, mat, m,n,count+1,v, min,l+1);
                        
                    }
                }
            }
            
            
        }
        if(i<m-1){
            if(v[i+1][j]==0){
                if(mat[i+1][j]<mat[i][j]){
                    v[i+1][j]=l+1;
                    this.dfs(i+1, j, mat, m,n,count+1,v, min,l+1);
                    
                }
            }
            else{
                if(mat[i+1][j]<mat[i][j]){
                    if(v[i+1][j]<(l+1))
                    {
                       v[i+1][j]=l+1;
                    this.dfs(i+1, j, mat, m,n,count+1,v, min,l+1);
                        
                    }
                }
            }
            
            
        }
        
        if(j>0){
            if(v[i][j-1]==0)
            {
                if(mat[i][j]>mat[i][j-1])
                {
                    v[i][j-1]=l+1;
                    this.dfs(i,j-1, mat, m,n,count+1,v, min,l+1);
                }
                
            }
            else{
                if(mat[i][j]>mat[i][j-1]){
                    if(v[i][j-1]<(l+1))
                    {
                        v[i][j-1]=l+1;
                    this.dfs(i,j-1, mat, m,n,count+1,v, min,l+1);
                        
                    }
                }
            }
        }
        if(j<n-1)
        {
            if(v[i][j+1]==0){
                if(mat[i][j]>mat[i][j+1])
                {
                    v[i][j+1]=l+1;
                    this.dfs(i,j+1, mat, m,n,count+1,v, min,l+1);
                }
                
            }
            else{
                if(mat[i][j]>mat[i][j+1]){
                    if(v[i][j+1]<(l+1))
                    {
                        v[i][j+1]=l+1;
                    this.dfs(i,j+1, mat, m,n,count+1,v, min,l+1);
                        
                    }
                }
            }
        }
        }     

    public int longestIncreasingPath(int[][] matrix) {
        
        this.res = 0;
        if (matrix.length==0 || matrix[0].length==0)
            return 0;
        int min = 1000000;
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                if( matrix[i][j]<min)
                    min=matrix[i][j];
            }
        }
        
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[i].length;j++){
                int[][] v = new int[matrix.length][matrix[i].length];
                v[i][j]=1;
                this.dfs(i,j,matrix, matrix.length, matrix[i].length, 1, v, min, 1);
            }
        }
        
        return this.res;
    }
}
     
