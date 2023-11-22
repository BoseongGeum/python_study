import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    
    if sentence == 'EOI':
        break

    lower_sentence = sentence.lower()
    if 'nemo' in lower_sentence:
            print("Found")
    else:
        print("Missing")
