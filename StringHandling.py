mystring = "Hello World!"

# printing
print mystring
print 'mystring is %s' % mystring

# string len
print len(mystring)

# string reverse
print ''.join(reversed(mystring))
print mystring[::-1]

# split string
print mystring.split() # split on whitespace
print mystring.split('o') # split with character o
print list(mystring) # split all characters

# case
print mystring.lower()
print mystring.upper()
print mystring.swapcase()

# count string occurrances
print mystring.count('o')
# TODO ignore case?

# replace
print mystring.replace('o','u')

# check if string contains string
print 'lo' in mystring

# join strings
print mystring+mystring
print mystring+str(1)

# string to int
print int('1')

# make array from strings
print (mystring, mystring)
