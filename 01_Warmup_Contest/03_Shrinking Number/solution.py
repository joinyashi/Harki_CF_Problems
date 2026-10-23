taking_pos_int = int(input())

count = 0

if taking_pos_int < 10:
    print(count)
else:
    while taking_pos_int > 10:
        a = taking_pos_int // 10
        b = taking_pos_int % 10
        taking_pos_int = a * b
        count += 1
    print(count)