################################################################################
#def inc(x):
#    return x + 1

#f = inc

#print f(10)

#function within a function
#def h(x):
#    return lambda y: x + y

#b = h(1)(3)
#print h(1)
#print h(2)
#print h(1)(3)
#print h(2)(5)

#Q3: h(1)(3) and h(2)(5) create closures.

#def f(x):
#    def g(y):
#        return x + y
#    return g

#print f(1)
#print f(1)(3)
################################################################################

def r1(x):
    return 'hello' * x

def r2(x):
    return 'goodbye' * x

def repeat(x):
    return lambda y: x*y

print r1(2)
print r2(2)
print repeat('cool')(3)
