#!/usr/bin/python3

a = 9
b = (4,2,1,5,6,3)
sum=0
for i, v in enumerate(b):
  sum += v  
  if sum > 9 :
    print('stop pada urutan ke ', i+1)
    break
