from collections import deque

def solution(n, wires):
    result = n
    
    for term_wire in wires:
        tree = {term_wire[0]}
        queue = deque([term_wire[0]])
        while queue:
            node = queue.pop()
            for wire in wires:
                if wire == term_wire or wire[0] in tree and wire[1] in tree:
                    continue
                elif node == wire[0]:
                    tree.add(wire[1])
                    queue.appendleft(wire[1])
                elif node == wire[1]:
                    tree.add(wire[0])
                    queue.appendleft(wire[0])
        
        gap = abs(2 * len(tree) - n)
        if gap < result:
            result = gap
        
    return result
