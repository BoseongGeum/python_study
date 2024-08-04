class Node:
    def __init__(self):
        self.children = {}
        self.is_end_of_numbers = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, numbers):
        current_node = self.root
        
        for number in numbers:
            if number not in current_node.children:
                current_node.children[number] = Node()

            current_node = current_node.children[number]

            if current_node.is_end_of_numbers:
                return False

        current_node.is_end_of_numbers = True

        return not current_node.children

def is_consistent(all_numbers):
    trie = Trie()

    for numbers in all_numbers:
        if not trie.insert(numbers):
            return False
    
    return True
    
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    all_numbers = []
    
    for _ in range(n):
        all_numbers.append(input().rstrip())

    if is_consistent(all_numbers):
        print('YES')
    else:
        print('NO')
