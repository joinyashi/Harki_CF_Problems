rounds = int(input())

for _ in range(rounds+1):
    L = int(input())
    R = int(input())

    interval_sum = 0

    for i in range(L, R + 1):
        interval_sum += i

    print(interval_sum)