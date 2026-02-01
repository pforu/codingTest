import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 10만 단위는 O(n^2)가 불가능, 봐줘도 만 단위
# 코드를 작성 전에 다른 풀이를 생각해야 함
arr.sort()

front = 0
rear = n-1

cnt = 0
while(front < rear):
    if x - arr[front] < arr[rear]:
        rear -= 1
    elif x - arr[front] > arr[rear]:
        front += 1
    else:
        cnt += 1
        front += 1
        rear -= 1

print(cnt)


# 체크 배열
cnt = [0] * 20000001
ans = 0
for i in range(len(arr)):
    pair = X - arr[i]
    ans += cnt[pair]
    cnt[arr[i]] += 1
# 나를 체크 배열에 넣음
# 내 앞에 있는 것 중에(체크 배열에 있는 것 중에) 페어가 되면
# ans 올리기