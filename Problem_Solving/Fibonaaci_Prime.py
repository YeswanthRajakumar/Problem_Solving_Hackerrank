from itertools import combinations
def isPrime(n):  
    if (n <= 1): 
        return False
   
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True

n1 = int(input())
n2 = int(input())
prime_list_1 =[]
for i in range(n1,n2):
    if isPrime(i):
        prime_list_1.append(i)
print(prime_list_1)

for i in range(len(prime_list_1)):
    for j in range(len(prime_list_1)):
            if prime_list_1[i] is not prime_list_1[j]:
                # print((prime_list_1[j]*10)+prime_list_1[j])