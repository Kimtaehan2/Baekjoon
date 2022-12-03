word=str(input()).upper()
word_no_copy=list(set(word))
count=[]

for i in range(len(word_no_copy)):
    count.append(word.count(word_no_copy[i]))
count_test=list(set(count))
if count.count(max(count))==count_test.count(max(count_test)):
    print(word_no_copy[count.index(max(count))])
    
else:
    print("?")