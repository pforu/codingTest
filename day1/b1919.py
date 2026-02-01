import sys
input = sys.stdin.readline

strlst1 = [0]*26
strlst2 = [0]*26
str1 = input().strip()
str2 = input().strip()

asc = ord('a')
for n in str1:
    strlst1[ord(n) - asc] += 1
for n in str2:
    strlst2[ord(n) - asc] += 1

lst = zip(strlst1, strlst2)
rst = [abs(a - b) for a, b in lst]

# rst+=abs(strlst1[i]-strlst2[i])
print(sum(rst))