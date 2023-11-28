# recursion approch 

#def sol(w1, v1, w, n):
#     if n == 0 or w == 0:
#         return 0
#     if w1[n - 1] > w:
#         return sol(w1, v1, w, n - 1)

#     else:
#         return max(v1[n - 1] + sol(w1, v1, w - w1[n - 1], n - 1), sol(w1, v1, w, n - 1))


# w1 = [1, 2, 4, 5]
# v1 = [1, 4, 5, 7]
# w = 7
# n = len(w1)

# print(sol(w1, v1, w, n))

# time O(2^n) | space O(n) > space for recursion call !

# memoization( 0/1 knapsack problem)


# def knapSack(w, v, W, n):
#     if n == 0 or W == 0:
#         return 0

#     if t[n][W] != -1:
#         return t[n][W]

#     if w[n - 1] > W:
#         t[n][W] = knapSack(w, v, W, n - 1)
#         return t[n][W]

#     else:
#         t[n][W] = max(
#             v[n - 1] + knapSack(w, v, W - w[n - 1], n - 1), knapSack(w, v, W, n - 1)
#         )
#         return t[n][W]


# w1 = [1, 2, 4, 5]
# v1 = [1, 4, 5, 7]
# w = 7
# n = len(w1)

# t = [[-1 for _ in range(w + 1)] for _ in range(n + 1)]

# print(knapSack(w1, v1, w, n))

# time O(n*w) | space O(n) + O(n*w)

def knapsack(w, v, W,n):
    t=[[0]* (W+1) for i in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,W+1):
          
            if w[i-1] >j:
               t[i][j]= t[i-1][j]
            else:
                t[i][j]= max(v[i-1]+ t[i-1][j-w[i-1]],t[i-1][j])

    return t[n][W]

w=[8,16,32,40]
v=[50,100,150,200]
W=64
n=len(w)
print(knapsack(w,v,W,n))
# time O(n*w) | space O(n) + O(n*w)

