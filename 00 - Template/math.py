x=10
y=3

# +
z = x + y
print(x, '+', y, '=', z)

# -
z = x - y
print(x, '-', y, '=', z)

# x
z = x * y
print(x, '*', y, '=', z)


# :
z = x / y
print(x, ':', y, '=', z)


# exponential
z = x ** y
print(x, '**', y, '=', z)

# mod
z = x % y
print(x, '%', y, '=', z)

# floor round
z = x // y
print(x, '//', y, '=', z)

#prior
a = 3
b = 2
c = 4

d = a ** b * c + a / b - b % c // a
print(a,'**',b,'*',c,'+',a,'/',b,'-',b,'%',c,'//',a, '=', d)

#priority 
'''
    1. ()
    2. exponen **
    3. * / ** % //
    4. + -
'''