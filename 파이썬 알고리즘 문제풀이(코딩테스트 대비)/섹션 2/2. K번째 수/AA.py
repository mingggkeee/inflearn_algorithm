T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr2 = arr[s-1:e]
    arr2.sort()
    print('#%d %d' %(i+1, arr2[k-1]))