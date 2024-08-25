# problem 4: count of subset sum 

def sol(arr, tar):
    n=len(arr)
    t=[[0]*(tar+1) for _ in range(n+1)] # 0 because there's no element to make the sum
    for i in range(n+1):
        t[i][0] =1 # we get 1 element although it's empty but it's count is 1 so, that's count !

    for i in range(1, n+1):
        for j in range(1, tar+1):
            if arr[i-1] > j:
                t[i][j]= t[i-1][j]

            else:
                t[i][j] = t[i-1][j] + t[i-1][j- arr[i-1]] # just here , (+) sign when in problem 2 , we just use (or) 
 
    return t[n][tar]

print(sol([2,3,5,8,10],10)) # output: 3
