import numpy as np
import matplotlib.pyplot as plt
import os

#def getsize('IQ.hex'):
 #   st = os.stat('IQ.hex)
  #  return st.st_size

a = os.path.getsize('IQ.hex')
print a ,"(byte)"

f = np.fromfile('IQ.hex', dtype=np.int16, count=10) 
print f


