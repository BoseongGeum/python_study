import sys
input = sys.stdin.readline

th, tm, ts = map(int, input().split(':'))
fh, fm, fs = map(int, input().split(':'))

if fs < ts:
    s = fs - ts + 60
    fm -= 1

else:
    s = fs - ts

if fm < tm:
    m = fm - tm + 60
    fh -= 1

else:
    m = fm - tm

if fh < th:
    h = fh - th + 24

else:
    h = fh - th

print(str(h).zfill(2)+':'+str(m).zfill(2)+':'+str(s).zfill(2))
