import sys
input = sys.stdin.readline

print("""n e
- -----------
0 1
1 2
2 2.5""")
result = 2.5
for i in range(3, 10):
    s = 1
    for j in range(1, i+1):
        s *= j
    s = 1 / s
    result += s
    print(f"{i} {result:.9f}") 
