import  numpy as np
a=np.random.randint(3,size=2880)
a=list(a)

def all_list(arr):
    result = {}
    for i in set(arr):
        result[i] = arr.count(i)
    return result
print all_list(a)