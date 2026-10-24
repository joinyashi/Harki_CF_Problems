s_n, e_n = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

count = 0

for num in range(s_n, e_n + 1):
    if is_prime(num):
        rev_num = int(str(num)[::-1])

        if is_prime(rev_num):
            count += 1

print(count)