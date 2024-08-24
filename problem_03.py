# problem 3: partitioning equal subset sum
# knapsack problem same as subset sum

# 1,11,5,5 output: true
# 
# 1,2,3,5 output: false
def sol(arr):
    it= sum(arr)
    if it %2 !=0: # if odd then, not possible 
        return False
    else: # if even, then just same as subset sum
        w=it//2 #just make the target half to see , if it's possible !
        n=len(arr)
        t=[[False]*(w+1) for _ in range(n+1)]
        for i in range(n+1):
            t[i][0]= True
  
        for i in range(1, n+1):
            for j in range(1,w+1):
                if arr[i-1] > j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j] or t[i-1][j-arr[i-1]]
  
        return t[n][w]
    
#print(sol([1,5,5,11]))
# it=sum([1,5,5,11]) =22
# problem seems like that, if we can make 11 from this array !

