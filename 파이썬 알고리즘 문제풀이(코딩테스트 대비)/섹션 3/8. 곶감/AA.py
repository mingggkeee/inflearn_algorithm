n = int(input())

num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

m = int(input())

command_list = []
for j in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k):
            num_list[h-1].append(num_list[h-1].pop(0))
    else:
        for _ in range(k):
            num_list[h-1].insert(0, num_list[h-1].pop())


res = 0
s = 0
e = n - 1

for i in range(n):
    for j in range(s, e+1):
        res += num_list[i][j]
    if i < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)