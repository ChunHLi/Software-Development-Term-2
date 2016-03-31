################################################################################

#Basics

#1

#nums = []
#for x in range(8):
#    nums.append(x)
#print nums


#2

#squares = []
#for x in range(8):
#    squares.append(x**2)
#print squares


#print [x for x in range(8)] #equivalent of 1
#print [x*x for x in range(8)] # equivalent of 2
#print [ (x, x*x, x*x*x) for x in range(8) ]

################################################################################

#Lesson

#p="myNoobPass1234"
#print p

#print [x for x in p] #creates a list of characters from a string
#print [x for x in "1234"]

#UC_LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#print [ x for x in p] 
#print [ x for x in p if x in UC_LETTERS ]
#checks what letters the word in the list.

#print [ 1 for x in p if x in UC_LETTERS ]
#gives a list of numbers and the length of that list is
#the amount of letters in the Upper Alphabet

################################################################################

def minThreshold(password):
    LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "1234567890"
    if ((len([x for x in password if x in LC_LETTERS]) > 0 and len([x for x in password if x in UC_LETTERS]) > 0) and (len([x for x in password if x in NUMBERS]) > 0)):
        return True
    else:
        return False

#print minThreshold("abc")
#print minThreshold("ABC")
#print minThreshold("123")
#print minThreshold("aBC")
#print minThreshold("AB1")
#print minThreshold("a12")
#print minThreshold("aB3")

def strengthTest(password):
    LC_LETTERS = "abcdefghijklmnopqrstuvwxyz"
    UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUMBERS = "1234567890"
    SYMBOLS = ".?!&#,;:-_*"
    rating = 0
    if (len([x for x in password if x in LC_LETTERS]) > 0):
        rating += 1
    if (len([x for x in password if x in UC_LETTERS]) > 0):
        rating += 1
    if (len([x for x in password if x in NUMBERS]) > 0):
        rating += 1
    if (len([x for x in password if x in SYMBOLS]) > 0):
        rating += 1
    if (len(password)/2 > 5):
        lengthPoints = 6
    else:
        lengthPoints = len(password)/2
    rating += lengthPoints
    return rating

print "Ayylmao should give 5: " + str(strengthTest("Ayylmao"))
