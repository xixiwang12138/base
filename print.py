

print(1, 5, 8, 'a')
print(7, 'bv')


print('我在星期一吃了{}个苹果'.format(76))
print('我在星期{1}吃了{0}个苹果'.format(78, '二'))
print('{0:.1f}'.format(2.66))


print('{:>30}'.format("abc"))
print('{:>30}'.format("b"))
print('{:>5}'.format('abcefg'))


print('{:^5}'.format("abbbbb"))

n = 100
for i in range(1, n+1):
    print('{:>3}'.format(i))

res1=["{0:>3}\n".format(i) for i in range(1, n+1)]
print(res1)
s = ""
for x in res1:
    s += x
print(s)

for x in res1:
    print(x)


n = 10
for i in range(1, n+1):
    print('{:>3} {:>4} {:>5}'.format(i,i**2,i**3))

n = 10
for i in range(1, n+1):
    print('{:3}{:3}{:3}'.format(i,i**2,i**3))


print('{:3}'.format('a'))