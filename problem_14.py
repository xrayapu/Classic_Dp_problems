#problem 14: topdown approch -> longest common subsequence 

def sol(x,y):
    n=len(x)
    m=len(y)
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]: #matching point
                t[i][j]= 1+t[i-1][j-1] # a, a => 1 

            else:
                t[i][j]= max(t[i-1][j], t[i][j-1]) # 

    return t[n][m]

print(sol('ashgshgfjf','smff'))
