for num in range(2,20):
    for x in range(2,num):
        if (x%2==0):            
            print(num,'equals',x,'*', num//x)
            break
    else:
         print(num,"is a prime number")
            