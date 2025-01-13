# matrix chain manipulation ! 

# abc matrix , a= [2*1], b=[1*3], c=[3*4] => (ab)c or a(bc) => ans = a(bc) 
# cost = arr[i-1] * arr[k] *arr[j]
def helper(arr, i,j):
    if i>= j:
        return 0
    ans= float('inf')
    for k in range(i,j):
        temp= helper(arr, i, k) + helper(arr,k+1, j)+ arr[i-1]*arr[k]*arr[j] #  
        ans= min(temp, ans)

    return ans

def sol(arr):
    n=len(arr)
    i=1
    j= n-1
    return helper(arr,i,j)

print(sol([1,2,3,4]))
