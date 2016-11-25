# calls  function with vars/params coming from dictionary

# sample function
def mytest(amount=0,other=10):
    print "received=",amount,other

# dictionary of vars
myvars = {'amount': 10, 'other': 0}

# ** means that the argument is a dictionary
mytest(**myvars)
