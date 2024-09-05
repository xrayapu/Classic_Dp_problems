# problem : coin change 2; minimum coins needed to make the target value

# 1,2,3 tar: 5

# 1+1+1+1+1
# 1+1+3 
# 1+1+1+2 
# 2+3 
# 1+2+2

# ans: 2>>> 2+3 is needed 

def sol(arr, w):
    n=len(arr)
    t=[[100000]*(w+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 0

    for i in range(1, n+1):
        for j in range(1, w+1):
            if arr[i-1] > j :
                t[i][j]= t[i-1][j]

            else:
                t[i][j] = min(t[i-1][j], 1+t[i][j - arr[i-1]]) # if inclueded , coin number is 1 already ! 

    if t[n][w] == 100000: #[2]  tar:3 -> not possible : so -1
        return -1
    return t[n][w]


print(sol([1,2,3],5)) 
