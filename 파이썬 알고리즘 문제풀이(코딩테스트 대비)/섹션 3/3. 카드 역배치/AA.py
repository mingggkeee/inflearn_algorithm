num_list = [i for i in range(1,21)]

for i in range(10):
    a, b = map(int, input().split())
    tmp = num_list[:a-1]
    tmp2 = num_list[a-1:b]
    tmp2 = tmp2[::-1]
    tmp3 = num_list[b:]
    num_list = tmp+tmp2+tmp3

for num in num_list:
    print(num, end=' ')