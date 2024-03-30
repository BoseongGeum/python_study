import sys
lst = []
tf = True
while tf:
    try:
        a = input()
        lst.append(a)
    except EOFError:
        tf = False
lst = "".join(lst)
lst = lst.replace(" ","") 

dic = {}
for i in lst: 
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1

dap = []
for key, value in dic.items(): 
    if max(dic.values()) == value:
        dap.append(key)

dap = sorted(dap)
print("".join(dap))
