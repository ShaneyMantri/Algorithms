/*
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

*/

class Solution {
    List<String> res = new ArrayList<String>();
    public void dfs(int n, String s, int lc, int rc) {
        if(lc>n)
            return;
        
        if(rc==lc){
            if(lc<n)
                this.dfs(n, s+"(", lc+1, rc);
            else
                this.res.add(s);
        }   
        
        else{
            this.dfs(n, s+"(", lc+1, rc);
            this.dfs(n, s+")", lc, rc+1);
            
        }
    
    }
    public List<String> generateParenthesis(int n) {
        this.res = new ArrayList<String>();
        if(n==0)
            return res;
        this.dfs(n,"", 0,0);
        return this.res;
    }
}
