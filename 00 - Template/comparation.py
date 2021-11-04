a = 4
b = 2

c = a > 5
print(c)

# is  for object comparation
x = 5 
y = 5

print('x = ', x, 'id =', hex(id(x)))
print('y = ', y, 'id =', hex(id(y)))

#compare with object in memory
z = x is y
print('x is y =', z)

# compare with literal
z = x == 5
print('x is y =', z)