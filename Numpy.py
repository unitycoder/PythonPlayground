import numpy as np # can alias library name to shorter

# create 1D linear array, integers
start = 0
end = 10
count = 5
arr = np.linspace(start,end,count,endpoint=False,retstep=False,dtype=np.int32)

for n in np.nditer(arr): #iterate array values
    print n, # 0,2,4,6,8

