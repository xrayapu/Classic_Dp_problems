## subset sum problem 
##arr= 2,3,5,8,10  tar= 11 output will be true/false , in this case true.

def sol(arr,w):
    n=len(arr)
    t=[[False]*(w+1) for _ in range(n+1)] 

# arr size 0 but sum=1,2,3,.... that's impossible , that's why False
# again t[0][0]= true because arr size =0 and sum =0 , that's possible with empty set. that's why true



    for i in range(n+1): # arr size =0,1,2,3,.... sum =0, with empty set it's possible        
        t[i][0]=True


    for i in range(1, n+1):
        for j in range(1,w+1):
            if arr[i-1] > j:
                t[i][j]= t[i-1][j]

            else:
                t[i][j]= t[i-1][j] or t[i-1][j-arr[i-1]]

    return t[n][w]

# arr=[3,4,12,5,2]
# w=9
# print(sol(arr,w))
