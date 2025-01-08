# problem 26: insert minimum number of character to make the string palindrome!

# same problem: in 22! just there we delete it and here we say, we add it ! but the code is same here also ! 

def sol(arr):
    tar= arr[::-1]
    n=len(arr)
    t=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if arr[i-1] == tar[j-1] :
                t[i][j]= 1+ t[i-1][j-1]

            else:
                t[i][j]= max(t[i][j-1], t[i-1][j])

    return n-t[n][n]

# print(sol('aabebcdd'))
