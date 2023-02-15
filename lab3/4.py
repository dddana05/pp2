def is_prime(x):
    x = int( x )
    if(x%2==0 and x!=2) or x==1:
        return False
    
    for i in range(3,x,2):
        if x %i==0:
         return False
    return True


def filter_primes(list):
    x=[]
    for i in list:
        if is_prime(i):
            x.append(i)
    return x

a=list(map(int,input().split()))

print(filter_primes(a))
