n, k = map(int, input().split())
 
small = []
large = []
 
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        small.append(i)
 
        if i != n // i:
            large.append(n // i)
 
factors = small + large[::-1]
 
if k <= len(factors):
    print(factors[k - 1])
else:
    print(-1)