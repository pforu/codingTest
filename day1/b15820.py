import sys
input = sys.stdin.readline

samp, syst = map(int, input().split())

for _ in range(samp):
    s, ans = map(int, input().split())
    if s!=ans:
        print("Wrong Answer")
        exit()

for _ in range(syst):
    s, ans = map(int, input().split())
    if s!=ans:
        print("Why Wrong!!!")
        exit()

print("Accepted")