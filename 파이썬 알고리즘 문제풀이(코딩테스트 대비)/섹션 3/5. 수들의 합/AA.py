n, m = map(int, input().split())

num_list = list(map(int, input().split()))
cnt = 0
tmp = 0
for i in range(len(num_list)):
    tmp += num_list[i]
    if tmp == m:
        cnt +=1
        tmp = 0
        continue
    elif i == len(num_list):
        break
    else:
        for j in range(i+1, len(num_list)):
            tmp += num_list[j]
            if tmp == m:
                cnt += 1
                tmp = 0
                break
            elif tmp > m:
                tmp = 0
                break

print(cnt)
