
def dfs(st,en,n, g,v,mat):
    mat[st][en]="Y"
    if en in g:
        for j in g[en]:
            if v[j]==0:
                v[j]=1
                dfs(st,j,n,g,v,mat)

t = int(input())
text_file = open("output.txt", "w")
for _ in range(t):
    n = int(input())
    inArray = list(input().strip())
    outArray = list(input().strip())
    g = {}
    for i in range(n):
        if outArray[i]=="Y":
            if i<(n-1) and inArray[i+1]=="Y":
                if (i) in g:
                    g[i].append(i+1)
                else:
                    g[i]=[i+1]
            if i>0 and inArray[i-1]=="Y":
                if (i) in g:
                    g[i].append(i-1)
                else:
                    g[i]=[i-1]    
    mat = [['N']*n for _ in range(n)]
    for i in range(n):
        mat[i][i]="Y"

    for i in range(n):
        v = [0]*n
        if i in g:
            if v[i]==0:
                v[i]=1
                dfs(i,i,n,g,v,mat)
    text_file.write("Case #{}:\n".format(_+1))
    for i in mat:
        text_file.write("".join(i)+"\n")

text_file.close()
