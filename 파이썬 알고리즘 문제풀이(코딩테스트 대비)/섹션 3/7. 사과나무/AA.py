n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

apple_sum = 0

idx = 1
lt = n//2
rt = n//2
for i in range(0, n//2):
    for j in range(lt, rt+1):
        apple_sum += num_list[i][j]
    lt -=1
    rt +=1

for i in range(n):
    apple_sum += num_list[n//2][i]

lt = 1
rt = n-1
for i in range(n//2+1, n):
    for j in range(lt, rt):
        apple_sum += num_list[i][j]
    lt += 1
    rt -= 1

print(apple_sum)