"""Given 2 strings A and B, check if A is present as a subsequence in B.
Input Format
First line of input contains T - number of test cases. Its followed by T lines, each line contains 2 space separated strings - A and B. 
Constraints
1 <= T <= 1000 
1 <= len(A), len(B) <= 1000 
'a' <= A[i],B[i] <= 'z' 
Output Format
For each test case, print "Yes" if A is a subsequence of B, "No" otherwise, separated by new line.
Sample Input 0
2
data gojdaoncptdhzay
algo plabhagqogxt
Sample Output 0
Yes
No"""
n=int(input())
for _ in range(n):
    a,b=input().split()
    l=len(a)
    m=len(b)
    i=j=0
    while i<l and j<m:
        if a[i]==b[j]:
            i+=1
        j+=1
    if i==l:
        print("Yes")
    else:
        print("No")
