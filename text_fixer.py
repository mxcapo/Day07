import sys


def open_and_read_file(corpus):
	"""let's try to get those numbers out"""

	f = open(corpus)


	for line in f:
		if len(line) < 50:
			continue
		elif line[0:7] == "Replies":
			continue
		else:
			line = line.strip()
			print line
	f.close()










def main():
	args = sys.argv

	input_text = args[1]

	open_and_read_file(input_text)

if __name__ == "__main__":
	main()