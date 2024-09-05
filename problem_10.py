# problem 10: coin change problem-1, maximum number of ways to make the coin possible. 
# 1,2,3 tar: 5

# 1+1+1+1+1
# 1+1+3 
# 1+1+1+2 
# 2+3 
# 1+2+2   
# total 5 ways 

# kind of subset sum problem , only unbound knapsack !
def sol(arr, tar):
    n= len(arr)
    t=[[0] * (tar+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1

    for i in range(1, n+1):
        for j in range(1,tar+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j]= t[i-1][j]+t[i][j-arr[i-1]]

    return t[n][tar]

arr=[1,2,3]
tar=5
print(sol(arr, tar))
