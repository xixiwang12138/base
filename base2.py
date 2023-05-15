# and
# or
# not

def check1(a, b):
    return a > b


def check2():
    print("hello, world")
    return 1 < 0


# if check1(2, 1) or check2():
#     print("hello")

# 短路运算符 or


# and

# if check1(2,1) and check2():
#     print("world")
# print(check1(2, 1))


# if condition: # 布尔值

# if 1 == 1:
#     print("hello")
#
# print(1==1)   # True

# 变量的类型是动态变化的，由当时的数据决定

list = ['a', 'b', 1, True]
empty_list = []
# print(type(empty_list))
#
#
# empty_list = 1
# print(type(empty_list))

list.append(2)
print(list)

# list.clear()
# print(list)

print(list.pop())  # 从尾部开始取出

print(list)

res = list[1]
list[1] = 0

print(list[1])
print(list)


# arr = ['关系', 2]
# arr2 = [1, 2]
# print(arr > arr2)



# print(list)
# list.append()



sub = [1, 2, 3]
part = [2, 3]
res = sub + part

# res = sub
# for i in part:
#     res.append(i)

res = sub*3


print(res)

print(type(res))





