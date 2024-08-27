# problem 6: give the count of subset sum when difference is given
#s1-s2=dif
#s1+s2=sum
#s1=(dif+sum )//2
#so, we just have to find how many number we can create from arr when target is s1. 
#problem then will be count subset sum ! 

# [1,1,2,3] dif:1 -> output: 3

def sol(arr,dif):
    it=sum(arr)
    w= (it+dif)//2
    n=len(arr)
    t=[[0]*(w+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1

    for i in range(1, n+1):
        for j in range(1, w+1):
            if arr[i-1] > j:
                t[i][j]=t[i-1][j]

            else: 
                t[i][j]= t[i-1][j] + t[i-1][j- arr[i-1]]

    return t[n][w]

# print(sol([1,3,1,2],1))
