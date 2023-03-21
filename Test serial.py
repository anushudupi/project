import serial
import numpy as np

pattern="\nabcdefg"
print(pattern[0])

# Open and configure serial port
ser = serial.Serial('COM5',25000000)
print('started')
i=0
while True:
    data = ser.read().decode() # Read a single character from the serial port

    if data == pattern[i]: # Check if the character matches the first character in the pattern
        
        i=i+1
        if i==8: # If all characters in the pattern have been matched
          
          bytes = ser.read(120001) # Read up to 1024 bytes
          print("pass")
          print(bytes[120000])
          i=0    

        #arr = np.frombuffer(bytes, dtype=np.int8)       
    elif data == pattern[0]:
        i=1
    else:
        
        i=0    


# Read bytes from serial port
