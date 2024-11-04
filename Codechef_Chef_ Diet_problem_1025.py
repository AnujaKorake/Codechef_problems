//problem link: https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DIET?tab=statement

t = int(input())
while t > 0:
    t -= 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    rem_diet = 0 
    possible = True

    for i in range(n):
        rem_diet += a[i]
        if rem_diet < k:
            print("NO", i + 1)
            possible = False
            break
        rem_diet -= k

    if possible:
        print("YES")