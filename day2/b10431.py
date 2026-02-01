import sys
input = sys.stdin.readline

NUM = 21

casenum = int(input())
rst = [0]*casenum

for line in range(casenum):
    testcase = list(map(int, input().split()))
    testrst = []
    for studnum in range(NUM):
        #print(testrst)
        stud = testcase[studnum]
        if studnum==0: #range(1, NUM)으로 처리하는 게 낫지
            continue
        elif studnum==1:
            testrst.append(stud)
        else:
            large = True
            for interstudnum in range(studnum-1):
                if stud<testrst[interstudnum]:
                    testrst.insert(interstudnum, stud)
                    rst[line] += studnum - interstudnum - 1
                    large = False
                    break
            if large:
                testrst.append(stud)
                #large 둘 필요 없이 그냥 밖에서 insert 처리해도 됨

for i in range(casenum):
    print(i+1, rst[i])

# 내 후에 줄 서는 애들 중 나보다 작은 애들의 수만큼 뒤로
# 실제로 움직일 필요가 없는 문제들이 많음
# 매핑을 쓰든가(줄세우기) 한꺼번에 처리하든가(징검다리) 반복주기를 찾든가(개미)
# 규칙과 특징을 관찰하는 게 중요함

h = list(map(int, input().split()))[::-1]
for i in range(20):
    for j in range(i + 1, 20):
        if h[i] > h[j]:
            cnt += 1