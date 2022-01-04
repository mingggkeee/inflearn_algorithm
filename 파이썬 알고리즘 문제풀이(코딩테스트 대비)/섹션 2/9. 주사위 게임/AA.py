from collections import Counter

n = int(input())

prize = []

for i in range(n):
    dice = list(map(int, input().split()))
    counts = Counter(dice)
    most_counts = Counter(dice).most_common(1)
    if most_counts[0][1] == 3:
        prize.append(10000+most_counts[0][0]*1000)
    elif most_counts[0][1] == 2:
        prize.append(1000+most_counts[0][0]*100)
    else:
        dice.sort(reverse=True)
        prize.append(dice[0]*100)

prize.sort(reverse=True)
print(prize[0])