class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        current = self.root
        for digit in number:
            if digit not in current.children:
                current.children[digit] = TrieNode()
            current = current.children[digit]
            if current.is_end_of_number:
                return False
        current.is_end_of_number = True
        return not current.children

def is_consistent(phone_numbers):
    trie = Trie()
    for number in phone_numbers:
        if not trie.insert(number):
            return False
    return True

# 입력 처리 부분
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
for _ in range(t):
    n = int(data[index])
    phone_numbers = data[index + 1:index + 1 + n]
    index += 1 + n

    if is_consistent(phone_numbers):
        print("YES")
    else:
        print("NO")
