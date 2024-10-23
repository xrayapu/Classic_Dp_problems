#problem 24: minimum number of insertion to make a string "a" into a palindrom

# x= agbcba , output: 1

# here if we get another 'g' add to the existing string , then we can get a palindrom  !
# so ans is 1

# we get a same problem in problem 18 !

# statment of problem 18: minimum number of deletion of a string to make it palindrom ! 

#  x= agbcba , output: 1

#there if we delete 'g' in existing string , then we can get a palindrom  !
# so ans is 1, so we just do the same code ! 

def sol(arr):
    n=len(arr)
    x=arr[::-1]
    t=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if arr[i-1]== x[j-1]:
                t[i][j]= 1+t[i-1][j-1]

            else:
                t[i][j]= max(t[i][j-1], t[i-1][j]) # lcs-> 5

    return n- t[n][n] # 6-5, add/delete = 1 word ! 

print(sol('agbcba'))

    
