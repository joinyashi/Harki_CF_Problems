n = int(input())

def is_prime(num):
    if num < 2:
        return False

    i = 2

    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


count = 0

for num in range(2, n + 1):
    if is_prime(num):
        count += 1

print(count)