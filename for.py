


# l = [1, 2, 3]
# for i in l:
#     print(i)


# [0, 0)
r = list(range(0))
print(r)

r2 = list(range(1, 3))
print(r2)


# [19, 10) -1
r3 = list(range(19, 10, -1))
print(r3)

d = [0,1,2]

seq = list(range(0, 101, 2))
res = sum(seq)
print(res)


# 求n的阶乘
def cal(n: int):
    if n <= 0:
        return 0
    l = list(range(1, n + 1))
    x = 1
    for i in l:
        x = x * i
    return x

print(cal(4))


str_list = ['1', '2', '3', '100']
num_list = []

for str in str_list:
    num_list.append(int(str))


# num_list2 = [int(s) for s in str_list]
#
# print("num_list2: ")
# print(num_list2)


print(str_list)
print(num_list)



# 我在星期{}吃了{}个苹果
arr = [23,54,5476,655,32,32,1]
week = ['一', '二', '三', '四', '五', '六', '七']


arr = [23,54,5476,655,32,32,1]
format_str = '我在星期{}吃了{}个苹果'
week = ['一', '二', '三', '四', '五', '六', '七']

l = [] # 每个元素都是列表


for index in range(0, 7):
    l.append([week[index], arr[index]])

print(l)

# key
# value


# with_week = [format_str.format(w) for w in week]
# print(with_week)
#
new_list = [format_str.format(o[0], o[1]) for o in l]
print(new_list)


res = sum([1/i for i in range(1, 21)])
print(res)

n = 100
res2 = sum([(-1)**(i+1)*(1/i) for i in range(1, n+1)])
res3 = sum([1/i if(i % 2 == 1) else -1/i for i in range(1, n+1)])
print(res2 == res3)





# a = '6'
# print(a*6)

n = 2

def translate(n: int):
    # return sum([10**i*6 for i in range(0, n+1)])
    return int('6'*n)

# res4 = sum([translate(i) for i in range(1, n+1)])

res4 = sum([translate(i) for i in range(1, n+1)])


# print(translate(2)) # 666
print(res4) # 732







res5 = sum([(-1)**(i+1)*(1/(2*i-1)) for i in range(1,26)])

print(res5)








