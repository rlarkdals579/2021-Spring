# Name : Kangmin Kim
# NetID KangKim
# SBUID : 111329652


open = ["[", "{", "("]
close = ["]", "}", ")"]


def is_balanced(str):
    newlst = []
    for i in str:
        if open.__contains__(i):
            newlst.append(i)
        elif close.__contains__(i):
            pos = close.index(i)
            if (len(newlst) > 0):
                if (open[pos] == newlst[len(newlst) - 1]):
                    newlst.pop()
            else:
                return "FALSE"
    if len(newlst) == 0:
        return "TRUE"
    else:
        return "FALSE"


print('type your string : ')
string = input()
print(string, "-", is_balanced(string))
