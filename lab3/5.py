from itertools import permutations

def per():
    s=input()
    print(' '.join(map(lambda x : ''.join(x),permutations(s))))
    per()
