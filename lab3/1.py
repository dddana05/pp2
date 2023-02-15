def my_fun(x):
 return lambda ounces,: x * ounces
mydoubler = my_fun(5)
print(mydoubler(28.3495231))


