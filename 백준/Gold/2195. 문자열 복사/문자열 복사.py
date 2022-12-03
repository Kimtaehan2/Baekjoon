import sys
input=sys.stdin.readline

S=input().strip()
P=list(map(str,input().strip()))
count=0
def find_min_str(word,S):
    if word in S: return True
    return False

def count_word_index(word1,word2,S):
    index1=1
    index2=-1
    len_word=len(P)
    while 1:
        if not find_min_str(''.join(word1),S): break
        if index1>len_word: break
        index1+=1
        word1=P[:index1]
        

    while 1:
        if not find_min_str(''.join(word2),S): break
        if abs(index2)>len_word: break 
        index2-=1
        word2=P[index2:]
               
    
    if index1>=abs(index2):
        del(P[:index1-1])
    else: del(P[index2+1:])
while P:
    count_word_index(P[0],P[-1],S)
    count+=1
print(count)