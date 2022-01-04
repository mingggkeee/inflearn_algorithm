N, K = map(int, input().split())

num_list = list(map(int, input().split()))

res = set()

for i in range(N):
    for j in range(i+1, N):
        for m in range(j+1, N):
            res.add(num_list[i]+num_list[j]+num_list[m])

num_list = list(res)

num_list.sort(reverse=True)

print(num_list[K-1])