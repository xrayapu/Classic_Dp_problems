# printing the elements of longest common subsequence in arrays !

# arr=abcde ,tar= abxdc => output: abc !


# arr= abcde, tar= abxce
# output=abce (output is 4 in length ! )


def sol(arr, tar):
    n=len(arr)
    m=len(tar)
    narr=[]
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1]== tar[j-1]:
                t[i][j]= 1+t[i-1][j-1]
                

            else:
                t[i][j]= max(t[i][j-1],t[i-1][j])

    i=len(arr)
    j=len(tar)
    while i>0 and j >0:
        if arr[i-1] == tar[j-1]:
            narr.append(arr[i-1])
            i-=1
            j-=1
        else:
            if t[i][j-1] > t[i-1][j]:
                j-=1
            else: i-=1

    narr.reverse()

    return ''.join(narr)
               

    

print(sol("abcde", "abxdc"))
