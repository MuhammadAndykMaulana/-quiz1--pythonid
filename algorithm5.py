a = 9
b = (4,2,1,5,6,3)

c = filter(lambda x: sum(b[:b.index(x)]) < a, b)
print('berhenti pada urutan ke %d.' % (len(c)))
