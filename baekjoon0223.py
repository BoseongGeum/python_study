import sys
imput = sys.stdin.readline

gradeDict = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5,
             'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
creditSum = 0
gradeSum = 0

for _ in range(20):
    objName, credit, grade = input().split()
    if grade != 'P':
        credit = float(credit)
        gradeSum += gradeDict[grade] * credit
        creditSum += credit
    
print(round(gradeSum / creditSum, 6))
