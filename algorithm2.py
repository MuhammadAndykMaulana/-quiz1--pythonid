from functools import reduce

def head(a):
    return a[0]

def tail(a):
    return a[1:]

def appendWhile(predicate, a, result=[]):
    if (predicate(result + [head(a)])):
        result.append(head(a))
        return appendWhile(predicate, tail(a), result)
    else:
        return result

a = 9 
b = (4,2,1,5,6,3)

panjang = len(appendWhile(lambda x: sum(x) <= a, b)) 
print('stop pada urutan ke-{}'.format(panjang+1))
