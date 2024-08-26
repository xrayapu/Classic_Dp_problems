# problem 5:  minimum subset sum difference 


def sol(arr):
    n=len(arr)
    w= sum(arr) # to set the range
    t=[[False]*(w+1) for _ in range(n+1)] # from this we just do the subset sum problem
    for i in range(n+1):
        t[i][0]= True

    for i in range(1, n+1):
        for j in range(1, w+1):
            if arr[i-1] > j:
                t[i][j]= t[i-1][j]

            else:
                t[i][j] = t[i-1][j] or t[i-1][j- arr[i-1]]

    # find minimum in last arr which elements are true 
    for j in range(w//2,-1,-1): # mid point to start 
        if t[n][j] == True:
            it= w - 2*j # s2-s1=>sum - s1-s1 => sum - 2s1

            break # 1st true ans will be the minimum , that's why break

    return it

print(sol([1,2,7]))  
