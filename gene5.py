def gensquares(N):
    for i in range(0,N): 
        yield i

for x in gensquares(10):
    print(x)