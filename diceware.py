
import sys
import random
import time
import linecache

def roll_dice():	
	return random.randint(1, 6)

def get_five_digits():
	n = ""
	for i in range(0,5):
		n += str(roll_dice())
	return n

def convert_to_base6(n):
	m =""
	for i in range(len(n)):
		m += str(int(n[i]) - 1)
	return m

def get_a_word():
	n = get_five_digits()
	m = convert_to_base6(n)
	base6 = int(m,6)
	offset = 3

	line_num = base6 + offset

	line = linecache.getline(wordlist, line_num)
	word = line.split()[1]
	#print n, m, line_num, word

	return word
	

if __name__ == '__main__':

	if len(sys.argv) > 1:
		wordlist = sys.argv[1]
	else:
		wordlist = "diceware.wordlist.asc"
	# print wordlist

	random.seed(time.clock())

	for i in range(0,6):
		print get_a_word(),