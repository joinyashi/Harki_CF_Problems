rounds = int(input())

for _ in range(rounds):
    L, R = map(int, input().split())

    sum_R = R * (R + 1) // 2
    sum_L = (L - 1) * L // 2

    interval_sum = sum_R - sum_L

    print(interval_sum)