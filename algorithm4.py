a = 9
b = (4,2,1,5,6,3)

d = 0
for c, i in enumerate (b):
  d += i-1
  if d > a:
    break

print("stop pada urutan ke {}".format (c))
