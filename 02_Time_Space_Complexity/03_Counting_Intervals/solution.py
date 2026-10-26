q = int(input())
 
for _ in range(q):
    t, l, r = map(int, input().split())
 
    if l > r:
        print(0)
 
    elif t == 1:
        print(max(0, r - l - 1))
 
    elif t == 2 or t == 3:
        print(max(0, r - l))
 
    elif t == 4:
        print(r - l + 1)
