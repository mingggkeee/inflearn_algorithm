n = int(input())

num_list = []

for i in range(n):
    num_list.append(list(map(int, input().split())))

max_sum = 0

# 행
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += num_list[i][j]
    if tmp > max_sum:
        max_sum = tmp

# 열
for i in range(n):
    tmp = 0
    for j in range(n):
        tmp += num_list[j][i]
    if tmp > max_sum:
        max_sum = tmp

# 대각
tmp = 0
for i in range(n):
    tmp += num_list[i][i]
if tmp > max_sum:
    max_sum = tmp

# 두번째 대각
tmp = 0
for i in range(n):
    tmp += num_list[i][n-1-i]
if tmp > max_sum:
    max_sum = tmp

print(max_sum)
