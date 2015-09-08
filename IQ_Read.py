import struct
import sys
fileData = open('IQ.hex','rb')

data_string = list(fileData.read(32))

print (data_string)
