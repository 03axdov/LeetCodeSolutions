from math import cos

curr = 0.5
for i in range(150):
    curr = cos(curr)**2
    
print(curr)