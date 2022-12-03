n = int(input())

def star(n):
    if n <= 3:
        return ['***','* *','***']

    arr = star(n//3)
    star_copy = []

    for i in arr:
        star_copy.append(i*3)

    for i in arr:
        star_copy.append(i+" "*(n//3)+i)

    for i in arr:
        star_copy.append(i*3)

    return star_copy

print("\n".join(star(n)))