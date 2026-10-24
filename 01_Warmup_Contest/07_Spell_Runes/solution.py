n = int(input())

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"

pattern = ""
count = 0

for i in range(1, n + 1):
    left = ""
    right = ""

    for j in range(i):
        if count % 2 == 0:
            char = letters[(count // 2) % 26]
        else:
            char = digits[(count // 2) % 10]

        left += char
        count += 1

    for j in range(i):
        if count % 2 == 0:
            char = letters[(count // 2) % 26]
        else:
            char = digits[(count // 2) % 10]

        right += char
        count += 1

    spaces = " " * (2 * n - 2 * i)

    print(left + spaces + right)