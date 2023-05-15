
# 1000(8)
# 111 -> 1110
a = 7
print(a >> 3)
print(a << 1) # 10000


for x in range(1, 1000):
    print(x << 1 == x * 2)