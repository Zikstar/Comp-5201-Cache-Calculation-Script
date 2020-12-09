# Author: Isaac Olukunle <bolanle93@yahoo.com>

#This is a simple python script
#That provided with the memory address as a Hex string (e.g abcd5678),
#number of bytes(B) in a line(e.g 256), and number of frames/sets e.g (65536)
#returns the Byte Ofset, the Line Number, Array Index, and Tag Value

#number of bytes in a line in decimal(B):  If you have
#number of offset bits "b". Convert it to B by calculating 2^b first.
#e.g if you don't know number of bytes in a line but you
#know the offset  is 8bits, then input 2^8 = 256, for this input parameter

#number of frames or sets (F/S): If you don't have the number of frames but
#instead you have frame number in bits, calculate F with F= 2^f
#.e.g If you know the frame number in bits is 10, then your input for this
#parameter is 2^16 = 65536

#Trying putting abcd5678, 256 and 65536 as input parameters, and comparing
#the answers to your answers by hand, if you're still not clear on what this
#program does.

#Obviously ignore the "0x", at the start of every answer.

def hexMod(hex_a, hex_b):
    a = int(hex_a, 16)
    b = int(hex_b, 16)

    return hex(a%b)

def hexDiv(hex_a, hex_b):
    a = int(hex_a, 16)
    b = int(hex_b, 16)

    return hex(a//b)

hex_a = input("Hex1(Memory Address):")
b = input("No of bytes in the line(B) in decimal:")
hex_b = hex(int(b))
frame = input("No of frames/sets(F/S) in decimal:")
hex_frame = hex(int(frame))

print("Byte Offset:" + hexMod(hex_a, hex_b))
line_number = hexDiv(hex_a, hex_b)
print("Line Number:"+ line_number )
print("Array Index:" + hexMod(line_number, hex_frame))
print("Tag Value:" + hexDiv(line_number, hex_frame))

