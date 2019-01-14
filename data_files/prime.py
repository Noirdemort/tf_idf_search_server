import math

def isPrimeNumber(n):
    
    # Returns True if n is prime number else False

    # Make sure n is a positive integer
    # if not then make it positive intger
    n = abs(int(n))

    # ----- some simple and fast tests ---------
    
    # The number n is less 2 i-e 0 or 1
    if n < 2: return False
    
    # The number n is 2
    if n == 2: return True

    # The number n is even then not prime
    if n % 2 == 0: return False

    # Check odd numbers less than the square root of the given number n for possible factors 
    r = math.sqrt( n )
    
    # start from 3, we have already test for 0, 1 and 2
    x = 3 
    while x <= r:
        if n % x == 0: return False  # A factor was found, so number is not prime
        x += 2 # Increment to the next odd number

    # No factors found, so number is prime  
    return True 
    

# check for prime number
n = int(input())
for _ in range(n):
    zord = "NO"
    k = int(input())
    addList = []
    for i in range(2,k//2+1):
        addList.append(tuple((i,k-i)))
#     print(addList)
    
    for i in addList:
        zord = "NO"
        factOne = []
        factTwo = []
        flag1 = False
        flag2 = False
        j = i[0]
        l = i[1]
        for k in range(2,j//2):
            if j%k==0:
                factOne.append(tuple((k,j//k)))
#         print(factOne, "Boi")
        for m in factOne:
            if isPrimeNumber(m[0]) and isPrimeNumber(m[1]):
#                 print(m, "-----> Hola")
                flag1 = True
                break
        if flag1:
            for k in range(2,l//2):
                if l%k==0:
                    factTwo.append(tuple((k,l//k)))
#             print(factTwo,"---------------------->ZUi")
            for m in factTwo:
                if isPrimeNumber(m[0]) and isPrimeNumber(m[1]):
#                     print("gola")
                    flag2 = True
                    break
        if flag1 and flag2:
            print("YES")
            zord = False
            break
    if zord:
        print(zord)
