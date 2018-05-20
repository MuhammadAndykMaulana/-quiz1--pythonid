#usr/bin/python
a=9
b= (4,2,1,5,6,3)
for i in b:
  if sum(b[:b.index(i)]) > a:
    print('stop pada urutan ke ', b.index(i))
    break
