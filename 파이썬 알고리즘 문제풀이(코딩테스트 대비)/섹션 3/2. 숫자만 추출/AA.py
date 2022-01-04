first_string = input()
res = 0

for letter in first_string:
    if letter.isdecimal():
        res = res*10+int(letter)

print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1


print(cnt)
