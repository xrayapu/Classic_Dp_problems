# problem :16 print the longest common subsequence

# arr= abcde, tar= abxce
# output= abce (output is 4 in length ! )


def sol(arr, arr2):
    n=len(arr)
    m=len(arr2)
    narr=[]
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if arr[i-1]== arr2[j-1]:
                t[i][j]= 1+t[i-1][j-1]
                

            else:
                t[i][j]= max(t[i][j-1],t[i-1][j])


    i=n
    j=m

    while i>0 and j>0 :
        if arr[i-1]== arr2[j-1]: # because array starts from 0
            narr.append(arr[i-1])

            i-=1
            j-=1

        elif t[i][j-1] > t[i-1][j]: # go to the maximum side ! 
            j-=1

        else: i-=1

               

    return ''.join(narr[::-1]) 

print(sol('abcde','abxce')) #output= abce

