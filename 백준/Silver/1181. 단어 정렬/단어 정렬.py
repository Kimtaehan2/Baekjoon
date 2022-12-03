n=int(input())
word=[]

for i in range(n):
    word.append(str(input()))

word_set=list(set(word))
word_sort=[]
for i in word_set:
    word_sort.append([len(i),i])

word_sort_copy=sorted(word_sort)

for i in range(len(word_sort)):
    print(word_sort_copy[i][1])