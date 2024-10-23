# problem-23: if string "a" is a subsequence of string "b" ?


# video 31: is subsequence ! 

# in video , they use, lcs and answer, but gives a error on
#leetcode ! so, although we code as they do , but the answer is
# the second one for this problem !

# 1st answer likewise as video! 

def sol_but_not_fully_ok(arr,tar):
    n=len(arr)
    m=len(tar)
    M=[]

    t=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            #print("deg",arr[i-1], tar[j-1])
            if arr[i-1]== tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]
                M.append(tar[j-1])
                print(M)

            else:
                t[i][j]= max(t[i][j-1], t[i-1][j])

    M="".join(M)
    if M == tar:
        return True, M
    else: return False

# print(sol_but_not_fully_ok('avsbec','bb'))

# 2nd answer:

def sol(arr,tar):
    n=len(arr)
    m=len(tar)
    narr=[]
    while n>0 and m>0:
        if arr[n-1]==tar[m-1]:
            narr.append(tar[m-1])
            n-=1
            m-=1
        else:
            n-=1 # just skip the array not the target ! 

    narr=''.join(narr)
    #print(narr)
    return narr== tar

# print(sol('avsbec','bb'))

