#problem 7: target sum, after using + or - sign how much number can be make the target

# arr: 1,1,2,3 tar: 1 => output: 3

# 1,1,1,1,1 tar:3 => output:5
# [1,0] ,tar: 1 => output: 2
#[1,0,0] , tar:1 => output:4


def sol(nums,tar):
    arr=[]
    p=0
    # here 0 not counted , so, we just skip the 0 for half solution
    for num in nums:
        if num !=0:
            arr.append(num)
        else:
            p+=1
            z=1 # 0 in the array
    tar=abs(tar) # target must be abs form ! 
    w=(tar+ sum(arr))//2  #count subset sum
    n=len(arr)
    if tar > sum(arr) or (tar+sum(arr)) %2 !=0: return 0 # edge case  fact
    t=[[0] *(w+1) for _ in range(n+1)]
    for i in range(n+1):
        t[i][0]= 1

    for i in range(1, n+1):
        for j in  range(1, w+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]

            else:
                t[i][j]= t[i-1][j] + t[i-1][j- arr[i-1]]
    if z==1: # 0 in the array
    
        return t[n][w] * pow(2,p) # ans *pow(2,count of 0)
    
    else:
        return t[n][w] # ans ! 
    

print(sol([1,0,0,0,0,0,0,0,0],1))
