import sys
input = sys.stdin.readline

string = input().strip()
for ch in string:
    ascii = ord(ch)
    print(chr(ascii+32), end='') if ascii<97 else print(chr(ascii-32), end='')