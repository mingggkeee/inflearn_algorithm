n = int(input())

math_score = list(map(int, input().split()))

math_avg = round(sum(math_score) / n)

best_num = 0
best_idx = 0
diff = 100000000

for idx, score in enumerate(math_score):
    tmp = abs(score-math_avg)
    if tmp < diff:
        diff = tmp
        best_num = score
        best_idx = idx+1
    elif tmp == diff:
        if score > best_num:
            best_num = score
            best_idx = idx+1


print(math_avg, best_idx)

