# converts int to 4-byte bytearray (big-endian or little-endian)
# modified from http://stackoverflow.com/a/25298778/5452781

def int2bytes(i, bigEndian=True):
    i = i % 4294967296
    n4 = i % 256
    i = i / 256
    n3 = i % 256
    i = i / 256
    n2 = i % 256
    n1 = i / 256
    if bigEndian:
        return [int(n4),int(n3),int(n2),int(n1)]
    else:
        return [int(n1),int(n2),int(n3),int(n4)]

# http://stackoverflow.com/a/386830/5452781
def bytes2int(b, bigEndian=True):
    if bigEndian:
        return (b[3] << 24) + (b[2] << 16) + (b[1] << 8) + b[0]
    else:
        return (b[0] << 24) + (b[1] << 16) + (b[2] << 8) + b[3]
        


# test
n= 16000

# convert to big-endian bytearray
b1 = int2bytes(n)
print b1

# convert to little-endian bytearray
b2 = int2bytes(n,False)
print b2

# convert from big-endian bytearray to int
v1 = bytes2int(b1)
print v1

# convert from little-endian bytearray to int
v2 = bytes2int(b2, False)
print v2
