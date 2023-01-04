
s = 0
for i in range(5):
    score = int(input())
    if score < 40:
        s += 40
    else:
        s += score

print(s//5)
