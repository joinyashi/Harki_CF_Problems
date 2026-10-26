n = 12

count = 0
i = 1

while i * i <= n:

    if n % i == 0:
        if i * i == n:
            count += 1
        else:
            count += 2

    i += 1

print(count)