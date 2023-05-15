
import math
a, b = 2, 1

a -= 2
a = a - 2
# print(a)




def cal(x: float):
    y = 0.0
    if x <= 15:
        y = 4*x/3
    else:
        y = 2.5*x-17.5
    return '%.2f' % y

c = float(cal(4.0))*2
print(type(c))
print(c)



