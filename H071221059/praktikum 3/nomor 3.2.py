x = int(input())

a = 0
b = 1

for i in range (x):
    print(a, end = ' ')
    c = a+b
    a = b
    b = c
    
    
# a b c
# 0 1 2
# 1

# print: 
