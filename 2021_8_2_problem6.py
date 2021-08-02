
num = int(input())

l = []

for i in range(num) :
    age, name = map(str, input().split())
    age = int(age)
    l.append((age, name))

l.sort(key = lambda m: (m[0]))
# l.sort(key = lambda m: (m[0])


for m in l:
    print(m[0], m[1])