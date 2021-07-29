import math



while True:
    result = 1
    a = int(input())
    if a == 0 :
        break
    
    
    a = list(str(a))

    for i in range(math.floor(len(a))) :
        if a[i] != a[len(a)-i-1] :
            result = 0
            break

    if result == 0 :
        print('no')
    else :
        print('yes')
            
        
        
    
