num = int(input())
num_list = list(map(int, input().split()))

result = 1
count = 0
i = 0

def isPalindrome(a):
    a_len_half = len(a) / 2
    front = a[0:int(a_len_half)]
    back = a[int(a_len_half):len(a)]
    back.reverse()

    if front == back :
        return True
    else :
        return False



while i < len(num_list):
    for j in range(i+1, len(num_list), 2):
        a = num_list[i:j+1]

    
        if i==0 and len(num_list) == len(a):
            count = -1
            result = 0
            break

        if isPalindrome(a) == True :
            i = j+1
            count = count + 1
            break
        if isPalindrome(a) == False :
            i = j + 1
        if isPalindrome(a) == False and j == len(num_list)-1:
            count = -1
            result = 0
            break

    if result == 0 :
        break

print(count)

