"""

	Basic Python Command Line Tool
	
	Author: Tina Aquino

"""

import getopt
import sys

def ascii(list):
	list = map(int, list)
	asciiVal = 0;
	for i in list:
		print "\nPlease note that the ASCII table has 128 characters, \nwith values from 0 through 127 \n"
		print 'ASCII value = ', chr(i)

def binary(list):
	list = map(int, list)
	binaryVal = 0;
	for i in list:
		print "Binary value = ", bin(i)

def searchFile(filename, search):
	count = 0;
	try:
		file = open(filename + ".txt", "r+")
		for line in file:
			if search in line:
				count += 1
		print "'", search, "' is found in the file", count, "times."
		file.close()
	except IOError:
		print "Error. File not found."

def readFile(filename):
	try:
		file = open(filename + ".txt", "r+")
		print file.read()
		file.close()
	except IOError:
		print "Error. File not found."

def wordCount(filename):
	count = 0;
	try:
		file = open(filename + ".txt", "r+")
		for line in file:
			words = line.split()
			count += len(words)
		print "Word count of file: ", count
		file.close()
	except IOError:
		print "Error. File not found."

def countLines(filename):
	lines = 0;
	try:
		file = open(filename + ".txt", "r+")
		for line in file:
				lines += 1
		print "There are ", lines, " in this file."
		file.close()
	except IOError:
		print "Error. File not found."

def reverse(filename):
	try:
		file = open(filename + ".txt")
		print filename, ".txt in reverse order: \n"
		for line in reversed(list(open(filename + ".txt"))):
			print(line.rstrip())
		file.close()
	except IOError:
		print "Error. File not found."


def help():
	print("Enter '-a' to convert integer values to ASCII.")
	print("Enter '-b' to convert integer values to binary.")
	print("Enter '-s' to get the word count of the given term in the file.")
	print("Enter '-p' to print/ read a .txt file.")
	print("Enter '-w' to get the word count of file.")
	print("Enter '-l' to count the lines in the file.")
	printf("Enter '-r' to reverse the file by lines.")
	print("Enter -h' to show user options.")

def main():
	try:
		opts, arg = getopt.getopt(sys.argv[1:], "abspwlrh")
	except getopt.GetoptError as err:
		print str(err)
		usage()
		sys.exit(2)

	for x, y in opts:

		if x == "-a":
			list = sys.argv[2:]
			ascii(list)
			sys.exit()
		elif x == "-b":
			list = sys.argv[2:]
			binary(list)
			sys.exit()
		elif x == "-s":
			filename = sys.argv[2]
			search = sys.argv[3]
			searchFile(filename, search)
			sys.exit()
		elif x == "-p":
			filename = sys.argv[2]
			readFile(filename)
			sys.exit()
		elif x == "-w":
			filename = sys.argv[2]
			wordCount(filename)
			sys.exit()
		elif x == "-l":
			filename = sys.argv[2]
			countLines(filename)
			sys.exit()
		elif x == "-r":
			filename = sys.argv[2]
			reverse(filename)
			sys.exit()
		elif x in ("-h", "--help"):
			help()
			sys.exit()
		else:
			assert False, "Invalid arguments. Enter '-h' for options."

if __name__ == "__main__":
	main()