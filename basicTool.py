"""

	Basic Python Command Line Tool
	
	Author: Tina Aquino

"""

import argparse
import getopt
import sys

def ascii(list):
	list = map(int, list)
	asciiVal = 0;
	for i in list:
		print 'ASCII value = ', chr(i)

def binary(list):
	list = map(int, list)
	binaryVal = 0;
	for i in list:
		print "Binary value = ", bin(i)

def add(list):
	list = map(int, list)
	sum = 0
	for i in list:
		sum += i
	print 'Sum = ', sum

def subtract(list):
	list = map(int, list)
	difference = list[0]
	for i in list[1:]:
		difference -= i
	print 'Difference = ', difference

def multiply(list):
	list = map(int, list)
	product = list[0]
	for i in list[1:]:
		product *= i
	print 'Product = ', product

def divide(list):
	list = map(int, list)
	quotient = list[0]
	for i in list[1:]:
		quotient /= i
	print 'Quotient = ', quotient

def help():
	print("Enter '-i' to convert integer values to ASCII.")
	print("Enter '-a' followed by integers to add.")
	print("Enter '-s' followed by integers to subtract.")
	print("Enter '-m' followed by integers to multiply.")
	print("Enter '-d' followed by integers divide.")
	print("Enter '-h' to show user options.")
	print("Enter '-r' to read a .txt file. ")

def readFile(filename):
	try:
		file = open(filename + ".txt", "r+")
		print file.read()
		file.close()
	except IOError:
		print "Error. File not found."

def main():
	try:
		opts, arg = getopt.getopt(sys.argv[1:], "ibasmdhr")
	except getopt.GetoptError as err:
		print str(err)
		sys.exit(2)

	for x, y in opts:

		if x == "-i":
			list = sys.argv[2:]
			ascii(list)
			sys.exit()
		elif x == "-b":
			list = sys.argv[2:]
			binary(list)
			sys.exit()
		elif x == "-a":
			list = sys.argv[2:]
			add(list)
			sys.exit()
		elif x == "-s":
			list = sys.argv[2:]
			subtract(list)
			sys.exit()
		elif x == "-m":
			list = sys.argv[2:]
			multiply(list)
			sys.exit()
		elif x == "-d":
			list = sys.argv[2:]
			divide(list)
			sys.exit()
		elif x in ("-h", "--help"):
			help()
			sys.exit()
		elif x == "-r":
			filename = sys.argv[2]
			readFile(filename)
			sys.exit()
		else:
			assert False, "Invalid arguments. Enter '-h' for options."
main()