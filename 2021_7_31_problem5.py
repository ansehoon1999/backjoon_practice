
num = int(input())
l = list(map(int, input().split()))

find = False

for i in range(num-1, 0, -1) :
    if l[i-1] < l[i] :
        for j in range(num-1, 0, -1) :
            if l[i-1] < l[j] :
                l[i-1], l[j] = l[j], l[i-1]
                l = l[:i] + sorted(l[i:])
                find = True
    if find :
        print(*l)
        break
if not find :
    print(-1)


