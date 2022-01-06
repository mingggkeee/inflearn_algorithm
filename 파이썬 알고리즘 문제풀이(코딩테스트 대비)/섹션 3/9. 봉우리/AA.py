n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))
num_list.insert(0, [0]*n)
num_list.append([0]*n)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for x in num_list:
    x.insert(0, 0)
    x.append(0)


cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(num_list[i][j] > num_list[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)