
a = int(input())

c = input()
b = list(c)

for i in range(len(b)) :
    print(a * int(b[len(b) - 1 - i]))

print(a * int(c))