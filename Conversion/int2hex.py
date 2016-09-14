i = 255
h = "%0.4X" % i
print h
# output: 00FF

i = 255
h = "%0.2X" % i
print h
# output: FF

i = 255
h = "0x%0.2X" % i
print h
# output: 0xFF
