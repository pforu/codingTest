import sys
input = sys.stdin.readline

n = int(input())
person = {}
for i in range(1, 201):
    person[i] = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    person[age].append(name)
person = sorted(person.items())
for item in person:
    for per in item[1]:
        print(item[0], per)



class Member:
    # age, name, idx
    def __init__(self, age: int, name: str, idx: int):
        self.age = age
        self.name = name
        self.idx = idx
#축약형 찾아 쓰기
#쓸 게 많아지면 이렇게 객체로 빼도 ㄱㅊ
# members.append(Member(int(age), name, i))

# members.sort(key=lambda x: (x.age, x.idx)) 
# stable 속성, idx 필요없음 