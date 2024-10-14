# longest palindromic subsequence problem .
#Given a string s, find the longest palindromic subsequence's length in s.
#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.


# just the lcs solutuion will be here! because this problem's requarement is the same as lcs.


def sol(s):
    tar=s[::-1]
    n=len(s)

    t=[[0]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1]== tar[j-1]:
                t[i][j]= 1+ t[i-1][j-1]

            else: 
                t[i][j] = max(t[i-1][j], t[i][j-1])


    return t[n][n]

print(sol('BBABCBCAB'))


#leetcode also passed with this code ! 
