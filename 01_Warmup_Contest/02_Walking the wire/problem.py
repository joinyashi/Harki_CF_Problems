no_of_testcases = int(input())

for i in range(no_of_testcases):
    color_knots = list(input())

    result = "YES"

    if len(color_knots) % 2 == 0:
        result = "NO"

    for j in range(len(color_knots) // 2):
        if color_knots[j] != color_knots[-(j + 1)]:
            result = "NO"
            break

    print(result)