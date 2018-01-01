import sys

print('this program shows you the binary and hexa version of your decimal number')
dec = int(input('enter a number : '))
bin(dec)
hex(dec)
print ("\nthe decimal value " ,dec, ": ")
print ("in binary is :",format(dec, 'b'))
print ("in hexadecimal is :",format(dec, 'x'))
print("\n\npress enter to quit")
input()
