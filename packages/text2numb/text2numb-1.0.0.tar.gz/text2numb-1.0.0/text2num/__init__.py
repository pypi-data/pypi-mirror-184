#!/usr/bin/env python3

# ======= DOCS ======= #

'''


Welcome to text2numb!
text2numb is a simple python module designed to convert text to a number and back again. It can be used in multiple ways, for example:
+ Cryptography (mathamatical operations such a division can be used on converted text. This is not reversable without the number that modified the converted text, and is practically impossible to crack by brute-force (or at least I think it is... )).
+ Compression (by using the operation oppisite of "to the power of" - this "reverse operation" could be easily implemented in a python function).
+ Whatever else you can think of... 


MAIN FUNCTIONS: 
+ text2numb(string)  - Converts text to numbers!
+ numb2text(integer) - Converts numbers to text!

SETUP FUNCTIONS:
+ setup(maxdigits=900000000) - Used to set the "int_max_str_digits" with sys. Called on import, should not be re-called unless truly necessary. 
								See PYPI page for more.

VARIABLES:
+ version			-		Module version
+ author			- 		Module author
+ digs				- 		Alphabet used in backend function "_int2base"
+ max_before_setup	-		The vaule of "int_max_str_digits" before setup(...) was called on import.

EXAMPLE USAGE OF CONVERSION FUNCTIONS:

# Import module
import text2numb

# Create text
text = 'Hello, world!'

print('Origional data: ')
print(text)

# Convert text to a number
number = text2numb.text2numb(text)

print('Converted data: ')
print(number)

# Convert number back to text
text2 = text2numb.numb2text(number)

print('Result: ')
print(text2)

print('Checking equality... ')
print(text == text2)

DOCUMENTATION & FURTHER READING

Documentation can be found on the PYPI page for this module.
Please refer to that for any further information.

'''

# ======= VERSION ======= #
version = '1.0.0'
author = 'PigeonNation (+ Others >> See code for more)'

# ======= CREDITS ======= #

# Mostly By " PigeonNation "
# See below for more:

# -=-=-=-=-=-=- IMPORTANT -=-=-=-=-=-=- #
# The credits for the function "_int2base" go to:
# Alex Huszagh & Alex Martelli on StackOverflow.com
# Their StackOverflow awnser (and the question) can be found here:
# https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base?r=SearchResults&s=1%7C235.2771
# The author of this python module did not ask the origional question.
# -=-=-=-=-=-=- IMPORTANT -=-=-=-=-=-=- #

# ======= IMPORTS ======= #
import string							# Used for aquiring "digs" - 0-9 + a-z + A-Z.
from base64 import b16encode, b16decode # Used for converting back and forth from base 16.
import sys 								# Used for setting "int_max_str_digits" using the "set_int_max_str_digits" function.

# ======= VARIABLES ======= #

# Integer Max String Before Setup Function Called
max_before_setup = sys.get_int_max_str_digits()

# Stores the alphabet used in _int2base
digs = string.digits + string.ascii_letters

# ======= SETUP ======= #

# Setup Function - Sets "int_max_str_digits" using sys.
def setup(maxdigits=900000000):
	'''setup(maxdigits=900000000) - Sets "int_max_str_digits" to keyword argument "maxdigits" using sys. Called on import. Use this function if you want to change the "int_max_str_digits", or just use sys.set_int_max_str_digits(...) to do it. Warning! If set to a lower value, you may receive some trouble when attempting to convert large amounts of data using the text2numb(...) and numb2text(...) functions. Raising this value much higher may raise an OverflowError complaining about "int to large to convert to C int" or something along those lines. It is recommended to keep the "int_max_str_digits" to the one set by this function on import. Note: If you would like to see what the "int_max_str_digits" value was before this function was called, look into the "max_before_setup" variable avaliable in this module. '''
	
	# Set "int_max_str_digits" to the "maxdigits" keyword argument.
	sys.set_int_max_str_digits(maxdigits)

# Call Setup Function
setup() 

# ======= BACKEND ======= #

def _int2base(x, base):
	global digs
	
	'''Convert an integer to a base ranging from 2-36. Used only by the program converting to base 16. See code for Credits. '''
	if x < 0:
		sign = -1
	elif x == 0:
		return digs[0]
	else:
		sign = 1
		
	x *= sign
	digits = []
	
	while x:
		digits.append(digs[x % base])
		x = x // base
		
	if sign < 0:
		digits.append('-')
		
	digits.reverse()
	
	return ''.join(digits)
	
# Credits for functions here on: The Author of this module.
	
# Turns text into numbers!
def _enc_num(string):
	'''Converts text to numbers - Backend Function.'''
	es = string.encode() # Convert to bytes 
	bes = b16encode(es)  # Encode in base 16
	ees = bes.decode()   # Convert to string 
	return int(ees, 16)  # Convert from base 16 to base 10

# Turns numbers into text!
def _dec_num(integer):
	'''Converts numbers to text - Backend Function.'''
	vf = _int2base(integer, 16) # Convert from base 10 to base 16
	vf = vf.upper()				# Make all letters uppercase
	vf = vf.encode()			# Convert to bytes 
	bs = b16decode(vf)			# Decode from base 16 to bytes
	return bs.decode()			# Convert from bytes to text!

# ======= MAIN FUNCTIONS / USER FUNCTIONS ======= #

# text2numb(...) - Converts text to numbers!
def text2numb(string):
	'''text2numb(string) - Converts text (string arg) to numbers. Only to be used with strings. Should work with most, if not all, unicode characters (uses UTF-8 for str.encode() and bytes.decode()).'''
	return _enc_num(string) # Calls _enc_num(...)

# numb2text(...) - Converts numbers to text!
def numb2text(integer):
	'''numb2text(string) - Converts numbers (integer arg) to text. Only to be used with integers. Should work with most, if not all, unicode characters (uses UTF-8 for str.encode() and bytes.decode()).'''
	return _dec_num(integer) # Calls _dec_num(...)

# ======= MODULE STUFF ======= #

# Module things...
# __all__ definition below:
__all__ = {
	'setup': setup, 						# setup(...) function.
	'text2numb': text2numb, 					# text2numb(...) function.
	'numb2text': numb2text, 					# numb2text(...) function.
	'max_before_setup': max_before_setup, 	# max_before_setup variable.
	'digs': digs, 							# digs variable.
	'version': version, 					# version variable.
	'author': author						# author variable.
}

# ======= TESTS ======= #

# Main test function.
def test():
	print('# ======= TESTING ======= #')
	print('Int2Base Test:', _int2base(14, 9))
	print('Input String:\t\t Hello, world!')
	num = text2numb('Hello, world!')
	print('Number Generated:\t',num)
	txt = numb2text(num)
	print('Final Result\t\t', txt)
	print()
	print('Text == Input? ')
	if txt == 'Hello, world!':
		print('Checked ... True!!')
	else:
		print('Error! Text != Input!')
		
	print('# ======= TESTING ======= #')
	
	print()
	print('# ======= STATS ======= #')
	print('Variables:')
	
	print('MaxBF:   ', max_before_setup)
	print('Digs:    ', digs)
	print('Version: ', version)
	print('Author:  ', author)
	print('# ======= STATS ======= #')
	
	print()
	print('Final Result: ----------  ')
	print()
	print('😀😀 Yay! 👍👍 ')
	print('Run Succeeded!')
	print('------------------------  ')
	
	

# Test if called as __main__.
if __name__ == '__main__':
	test()