################################################################################

#def wrapper( f ):
#   def inner( *arg ):
#       return f( *arg )
#   return inner


#closure = wrapper(foo)
#closure( -2, 3, 'hello' )
#will run foo with the arguments -2, 3, 'hello' through wrapper

################################################################################

import time

def wrapper( f ):
   startTime = time.time()
   def inner( *arg ):
       print f.func_name
       return f( *arg )
   endTime = time.time()
   totalTime = endTime - startTime
   print "time to process: " + str(totalTime)
   return inner

@wrapper
def foo(*x):
    print x

foo( -2, 3, 'hello' )

#This will record how long the program takes



#print totalTime
