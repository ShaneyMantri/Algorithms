class Solution:
    ans = 10**13
    def __init__(self):
        pass
        

    def dfs(self,arr, fibo, i,n, step):
        global ans
        if i==(n-1):
            if self.ans>step:
                self.ans=step
            return
        
        for j in range(1,20):
            if (i+fibo[j])<n:
                if arr[i+fibo[j]]==1:
                    self.dfs(arr,fibo,i+fibo[j], n, step+1)
            else:
                return



    def fib(self, n):
        arr = [0]*(n)
        arr[0]=0
        arr[1]=1
        for i in range(2,n):
            arr[i]=arr[i-1]+arr[i-2]
        return arr

arr = [0, 0]
arr = [1]+arr+[1]
s = Solution()
fibo = s.fib(20)
fibo = fibo[2:]
print(fibo)
if (len(arr)-1) in fibo:
    print(1)
else:
    s.dfs(arr,fibo,0,len(arr),0)
    print(s.ans)
