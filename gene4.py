a=input()
b=input()
squares_generator = (i * i for i in range(a,b))

for i in squares_generator:
    print(i)