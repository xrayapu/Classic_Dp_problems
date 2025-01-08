# longest repeating subsequence ! 

# lcs problem ! 

# aabebcdd -> 3 ( abd) (repeated 2 times) just return the length here ! 

def sol(arr):
    tar= arr[::-1]
    n=len(arr)
    t=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i-1] == tar[j-1] and i != j: ##just add here to make cross point ! 
                t[i][j]= 1+ t[i-1][j-1]

            else:
                t[i][j]= max(t[i][j-1], t[i-1][j])

    return t[n][n]

print(sol('aabebcdd'))
