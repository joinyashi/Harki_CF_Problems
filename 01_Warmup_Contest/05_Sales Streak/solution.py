
n = int(input())
sales = list(map(int, input().split()))

current_length = 1
max_length = 1

current_start = 1
best_start = 1

for i in range(1, len(sales)):

    if sales[i] >= sales[i - 1]:
        current_length += 1

    else:
        current_length = 1
        current_start = i + 1

    if current_length > max_length:
        max_length = current_length
        best_start = current_start

print(max_length, best_start)
