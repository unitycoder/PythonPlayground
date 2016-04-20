import threading

myGlobalVar = "12345"

def myFunc():
    print "MyFunc() was called\n"

class myThread (threading.Thread):
    def __init__(self, myvar):
        threading.Thread.__init__(self)
        print "Init Thread - " + str(myvar)
    def run(self):
        global myGlobalVar # can access global variables
        print "\nAdd Thread mainloop here " + myGlobalVar

        myFunc() # can call functions

        # can loop inside thread if needed
        #while 1:
            #print 1


# Create new threads
myVariable = 10
thread1 = myThread(myVariable)

somethingElse = "Yes"
thread2 = myThread(somethingElse)

# Start new Threads (otherwise only __init__ is run
thread1.start()
thread2.start()

print "\nExit Main Thread"
