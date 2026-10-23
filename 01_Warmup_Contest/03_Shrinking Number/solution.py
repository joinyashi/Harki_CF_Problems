n = int(input())
count = 0

while n >= 10:
    product = 1

    for digit in str(n):
        product *= int(digit)

    n = product
    count += 1

print(count)