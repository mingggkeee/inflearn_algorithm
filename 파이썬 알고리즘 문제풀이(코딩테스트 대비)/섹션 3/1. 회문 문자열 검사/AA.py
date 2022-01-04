n = int(input())

for i in range(1, n+1):
    letter = input()
    letter = letter.lower()
    reversed_letter = letter[::-1]
    if letter == reversed_letter:
        print("#{} YES".format(i))
    else:
        print("#{} NO".format(i))
