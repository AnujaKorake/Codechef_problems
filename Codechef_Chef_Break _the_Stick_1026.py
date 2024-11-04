#problem statement link : https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/BREAKSTICK?tab=statement 


# cook your dish here
t = int(input())
while t>0:
    t -= 1 
    n,x = map(int,input().split())
    parity = []
    
    if x%2 != 0:
        print("YES")
    else:
        if n%2 == 0:
            print("YES")
        else:
            print("NO")