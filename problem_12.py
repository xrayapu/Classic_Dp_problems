# longest common subsequence 
#x= abcde ,y =ace => output: 3 (ace) in both point 
# in subsequence, it's not necessary that common items should be in serials. 

def sol(x,y,n,m):
    if n==0 or m==0:
        return 0
    
    if x[n-1] == y[m-1]: #x=abcde y=a_c_e_ (count will be start from last point) 
        return 1+ sol(x,y,n-1,m-1)
    
    else:
        return max(sol(x,y,n-1,m),sol(x,y,n,m-1))
    
x='abcde'
y='prt'
print(sol(x,y,len(x),len(y)))

# but it's get time limit 
