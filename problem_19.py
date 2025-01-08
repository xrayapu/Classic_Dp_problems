# problem: shortest common supersequence.

# print the length of shortest common supersequence.  

# arr= geek , tar= eke   => output: 5

# first calculate the lcs. then just (-) it! 
def sol(arr,tar):
    n= len(arr)
    m=len(tar)
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range (1, n+1):
        for j in range(1, m+1):
            if arr[i-1]== tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]

            else:
                t[i][j]= max(t[i-1][j], t[i][j-1])

    return n+m - t[n][m]


  # that's the result ! 


# printing the shortest common supersequence ! 


# a= geek , b= eke  => geeke/gekek ! both are right !!!



  def sol(arr,tar):
    n= len(arr)
    m=len(tar)
    t=[[0]*(m+1) for _ in range(n+1)]
    for i in range (1, n+1):
        for j in range(1, m+1):
            if arr[i-1]== tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]

            else:
                t[i][j]= max(t[i-1][j], t[i][j-1])

    i,j=n,m
    narr=[]
    # change points
    while i* j >0:
        if arr[i-1] == tar[j-1]:
            narr.append(arr[i-1])
            i-=1
            j-=1

        else:
            if  t[i][j-1] >t[i-1][j] : 
                narr.append(tar[i-1])
                j-=1

            else: 
                narr.append(arr[i-1])
                i-=1

    while i>0:
        narr.append(arr[i-1])
        i-=1

    while j>0 :
        narr.append(tar[j-1])
        j-=1

    
    narr.reverse()

    return "".join(narr)

print(sol("geek","eke"))

# output: gekek! 



  


      
