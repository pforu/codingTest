a = ['abc', 'abcd', 'bcdf', 'i']
from collections import deque
arr = deque(map(int, input().strip()[1:-1].split(',')))
print(arr)