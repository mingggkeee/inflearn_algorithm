n = int(input())
first_list = list(map(int ,input().split()))
m = int(input())
second_list = list(map(int, input().split()))

sum_list = first_list + second_list
sum_list.sort()

for num in sum_list:
    print(num, end=' ')