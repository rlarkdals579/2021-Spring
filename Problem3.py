# Name : Kangmin Kim
# NetID KangKim
# SBUID : 111329652

def apply_fun(a, even):
    return [x for x, y in enumerate(a) if (even(y))]


def even(x):
    return x % 2 == 0


a = []
n = int(input('Enter number of values: '))
for i in range(n):
    a.append(int(input('Enter values: ')))

print(apply_fun(a, even))
