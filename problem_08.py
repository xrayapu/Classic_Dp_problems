# unbound knapsack;
#here we can chose one item unlimited time. so the code is just little change 

def sol(wt,val,w,n):
    t=[[0]*(w+1) for _ in range(n+1)]
    

    for i in range(1,n+1):
        for j in range(1, w+1):
            if wt[i-1] > j:
                t[i][j]=t[i-1][j]

            else:
                t[i][j]= max(val[i-1]+ t[i][j- wt[i-1]],t[i-1][j]) # just little change ! t[i-1]in 0/1 knapsack

    return t[n][w]


wt=[1,3,4,5]
w=8
val=[10,40,50,70]
n=len(wt)

print(sol(wt,val,w,n))
