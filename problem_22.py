# problem 22: print shortest common supersequence ! 

# a=abcde b= abxdc => output: abxcde

# just like the length of shorest common supersequence 

def sol(arr, tar): #lcs
    n=len(arr)
    m=len(tar)
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1, m+1):
            if arr[i-1]== tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]

            else:
                t[i][j]= max(t[i][j-1], t[i-1][j])

    i,j=n,m
    narr=[]
    while i>0 and j> 0: # print lcs part
        if arr[i-1] == tar[j-1]:
            narr.append(arr[i-1])
            i-=1
            j-=1

        else:
            if t[i-1][j]> t[i][j-1]: # moving to up but collect the right element !
                narr.append(arr[i-1])
                i-=1

            else: 
                narr.append(tar[j-1]) # move right, collect up element ! 
                j-=1
# collect the remaining elements
    while i>0: # part 1
        narr.append(arr[i-1])
        i-=1

    while j>0: #part 2
        narr.append(tar[j-1])
        j-=1

    narr= "".join(narr)

    return narr

print(sol("abac","cab"))
