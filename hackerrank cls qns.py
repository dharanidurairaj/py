You are given an infinite 2-d grid with the bottom left cell referenced as (1,1). All the cells contain a value of zero initially. Let's play a game?

The game consists of N steps wherein each step you are given two integers a and b. The value of each of the cells in the co-ordinate (u, v) satisfying 1 ≤ u ≤ a and 1 ≤ v ≤ b, is increased by 1. After N such steps, if X is the largest number amongst all the cells in the rectangular board, can you print the number of X's in the board?

Input Format
The first line of input contains a single integer N. N lines follow.
Each line contains two integers a and b separated by a single space.

Output Format
Output a single integer - the number of X's.

Constraints
1 ≤ N ≤ 100
1 ≤ a ≤ 106
1 ≤ b ≤ 106

Sample Input

3
2 3
3 7
4 1
Sample Output

2
Explanation

#Assume that the following board corresponds to cells (i, j) where 1 ≤ i ≤ 4 and 1 ≤ j ≤ 7.

At the beginning board is in the following state:

0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 
After the first step we will obtain:

0 0 0 0 0 0 0
0 0 0 0 0 0 0
1 1 1 0 0 0 0
1 1 1 0 0 0 0 
After the second step we will obtain:

0 0 0 0 0 0 0
1 1 1 1 1 1 1
2 2 2 1 1 1 1
2 2 2 1 1 1 1 
Finally, after the last step we will obtain:

1 0 0 0 0 0 0
2 1 1 1 1 1 1
3 2 2 1 1 1 1
3 2 2 1 1 1 1 
So, the maximum number is 3 and there are exactly two cells which correspond to 3. Hence 2.#


CODE:

a=int(input())
l=[]
p=[]
k=[]
for i in range(0,a):
    l.append(list(map(int,input().split(" "))))
for i in range(len(l)):
    p.append(l[i][0])
    k.append(l[i][1])
h=min(p)*min(k)
print(h)


-----------------------------------------------------------------------------------------------------------------------------

n=int(input())
a=0
b=0
min1,min2=0,0
for i in range(n):
    a,b=map(int,input().split(' '))
    if(i==0):
        min1,min2=a,b
    if a<min1:
        min1=a
    if b<min2:
        min2=b
print(min1*min2)
--------------------------------------------------------------------------------------------------------------------------------



a=int(input())
b=[]
c=[]
for i in range(a):
    d,e = map(int, input().split())
    b.append(d)
    c.append(e)
print(min(b)*min(c))

