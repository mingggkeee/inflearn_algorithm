N, K = map(int, input().split())

arr = []

for i in range(1, N+1):
    if N % i == 0:
        arr.append(i)

try:
    print(arr[K-1])
except:
    print(-1)
