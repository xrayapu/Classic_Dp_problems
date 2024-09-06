
# problem 13: longest common subsequence (memoization formate)

def sol(x,y,n,m):
    if n==0 or m==0: # base case, without any word nothing returns
        return 0
    t=[[-1]*(m+1) for _ in range(n+1)] #memozition ! 
    if t[n][m] !=-1:
        return t[n][m]
    
    if x[n-1]== y[m-1]:
        t[n][m]= 1+ sol(x,y,n-1,m-1) # we got 1 latter common in both of them
        return t[n][m]
    
    else:
        t[n][m]= max(sol(x,y,n-1,m), sol(x,y,n,m-1)) # largest common asked ! that's why max 
        return t[n][m]
    
x='avbcde'
y='avd'
print(sol(x,y,len(x),len(y)))
