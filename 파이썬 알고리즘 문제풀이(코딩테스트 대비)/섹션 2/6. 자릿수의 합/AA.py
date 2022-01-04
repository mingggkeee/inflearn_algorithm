def digit_sum(x):
    sum = 0
    for i in x:
        sum += int(i)

    return sum


n = int(input())
num_list = list(input().split())
print_value = 0

max = 0

for i in range(len(num_list)):
    a = digit_sum(num_list[i])
    if a > max:
        print_value = int(num_list[i])
        max = a

print(print_value)
