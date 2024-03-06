from itertools import combinations
def prime(num):
    if num<2:
        return False
    for i in range (2,int(num**0.5)+1):
        if num % i==0:
            return False
        return True
def prime_list(number):
    return[(x,y) for x,y in combinations(number,2) if prime(x+y)]
n_l=[1,2,3,4,5,6,7,8,9]
print(prime_list(n_l))