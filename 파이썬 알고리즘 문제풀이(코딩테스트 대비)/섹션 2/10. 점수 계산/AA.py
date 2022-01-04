n = int(input())
ox_list = list(map(int, input().split()))

score = 0
cnt = 1
for i in ox_list:
    if i == 1:
        score += cnt
        cnt +=1
    else:
        cnt = 1


print(score)
