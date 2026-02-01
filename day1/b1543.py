import sys
input = sys.stdin.readline

line = input().strip()
word = input().strip()

rst=0
i=0
while(i < len(line)-len(word)+1): #시간복잡도 n^2
    #패턴찾기는 O(n)으로 해결 가능 
    if word[0] == line[i]:
        flag = 1 #find, match / True, false
        k = i #맞음 
        for j in range(len(word)):
            if word[j] != line[k]:
                flag = 0
                break
            k+=1
        if flag:
            rst+=1
            i = k-1 #or rst += len(word) - 1
    i+=1

print(rst)                             