# problem 20: minimum number of deletation and insertion to convert a string to another ! 

# kind of lcs problem, first find lcs from a and b.(ea). then just -> len(a)- length of lcs  and 

# len(b)- length of lcs

# input: a= heap , b= pea (lcs->ans:2(ea) , not 3(pea), cz here order matters)
# lcs=2(ea), 
# ans= len(a)-lcs and len(b)- lcs

# lcs
def helper(arr,tar):
    n=len(arr)
    m=len(tar)
    t=[[0]*(m+1) for _ in range(n+1)]
    ans=0# to count the result ! 
    for i in range(1, n+1):
        for j in range(1,m+1):
            if arr[i-1]== tar[j-1]:
                t[i][j]=1+t[i-1][j-1]
                #ans=max(ans,t[i][j])

            else:
                t[i][j]=max(t[i][j-1], t[i-1][j])

    return t[n][m]


# main part
  
def sol(arr, tar):
    it= helper(arr, tar)
    return [abs(len(arr)-it), abs(len(tar)-it)]
  
print(sol("heap",'pea'))
