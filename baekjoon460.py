import sys
input = sys.stdin.readline

n = int(input())

init_file = input().rstrip()
correct_file = input().rstrip()

if n % 2 == 0 and init_file == correct_file:
    print('Deletion succeeded')
elif n % 2 == 1:
    init_file = init_file.replace('0', '2')
    init_file = init_file.replace('1', '0')
    init_file = init_file.replace('2', '1')

    if init_file == correct_file:
        print('Deletion succeeded')
    else:
        print('Deletion failed')
else:
    print('Deletion failed')
