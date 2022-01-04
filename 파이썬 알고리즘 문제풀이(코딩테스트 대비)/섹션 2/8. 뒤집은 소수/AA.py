def reverse(x):
    res = 0
    while x>0:
        t=x%10
        res = res * 10 + t
        x = x // 10
    return res

def isPrime(x):

    if x == 1:
        return False

    for i in range(2, x//2 + 1):
        if x % i == 0:
            return False
    else:
        return True

n = int(input())

num_list = list(map(int, input().split()))

for num in num_list:
    reverse_num = reverse(num)
    if isPrime(reverse_num) == True:
        print(reverse_num, end=' ')
    else:
        continue

