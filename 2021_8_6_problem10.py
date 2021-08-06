
a, b = map(int, input().split())

a = int(str(a), 2)
b = int(str(b), 2)

c = a + b
c = format(c, 'b')
print(c)
