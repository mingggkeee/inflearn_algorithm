n, m = map(int, input().split())

num_list = list(map(int, input().split()))
cnt = 0
lt = 0
rt = 1
tot = num_list[0]

while True:
    if tot < m:
        if rt < n:
            tot += num_list[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= num_list[lt]
        lt += 1
    else:
        tot -= num_list[lt]
        lt += 1


print(cnt)
