
"""
1. 可以通过序号访问
2. 是一种集合（数据类型）
3. 从0开始

列表、元组、字符串、Unicode字符串、buffer对象和xrange对象


(1) 通过索引访问:
 a. 越界
 b. 负数(-1, -n)
 c. 正书(0, n-1)

(2) 截取：
 a. 两个参数：左闭右开
 b. 一个参数
    i. s[1:]
    ii. s[:n-2]
 c. 索引中出现负数? 稳定性，不会逆序
 d. 三个参数：step 步长
    i. step < 0， 可以实现逆序

(3) 复制
(4) in - not in
  - 对于 str 来说：判断子串
  - 对于 list 来说：是否为list中某个元素，不是子list
"""


# 负数索引
s = "abcdef"
print(s[1:-3]) # bc
print(s[-1:4] == "") # True
print(s[:-2]) # abcd

# 逆序
print(s[::-2])

# 复制序列
s1 = [0, 1, 4]
s2 = s1[:]
s2[0] = 2
print(s1)


# 检查是否在: in
print([0, 1] in s1)
print(2 not in s1)



str1 = "abcde"
str2 = "ace"
print(str2 in str1)

