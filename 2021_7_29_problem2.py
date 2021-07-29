


while True:
    count = 0

    x1 = {}
    x2 = {}
    a, b = map(int, input().split())

    x1 = set(map(str,input().split()))
    x2 = set(map(str, input().split()))

    print(len(x1 ^ x2))
