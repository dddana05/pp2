import statistics
def my_fun(lst):
    return sum(lst)/len(lst)
lst=[1,2,3,4,5,6,7]
a=my_fun(lst)
print(round(a,2))
print(statistics.median(lst))
