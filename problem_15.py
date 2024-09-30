# problem 15: longest common substring -> veriation of longest common subsuquence(lcs)

# arr= abcde ,tar =abxce =>common substrings- ab,c,e => output : 2(ab) 

def sol(arr, tar):
    n=len(arr)
    m=len(tar)
    ans=0
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1] == tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]
                ans= max(ans,t[i][j]) # find longest here !  

            else:
                t[i][j]=0 #if not same sequence break and we get 0

    return ans

print(sol('abcde','abxce')) # output:2 
