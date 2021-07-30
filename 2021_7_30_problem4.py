
n, m = list(map(int, input().split()))

d = {}

for i in range(n):
    group = input()
    num = int(input())

    tmp = []
    for j in range(num) :
        member = input()
        tmp.append(member)

    d[group] = tmp



for i in range(m) :
    string = input()
    num = int(input())

    if num == 0 : #팀 이름이 주어짐
        for key, val in d.items() :
            if key == string :
                val = sorted(val)
                for i in range(len(val)):
                    print(val[i])



    elif num == 1: #맴버 정보 입력
        for key, val in d.items():
            if string in val :
                print(key)


