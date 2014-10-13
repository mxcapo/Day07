import sys


def open_and_read_by_line(corpus):
	"""removing comment and reply lines from tfln"""

	f = open(corpus)


	for line in f:
		if len(line) < 50:
			continue
		elif line[0:7] == "Replies":
			continue
		else:
			line = line.strip()
		return line


	f.close()

def open_and_read_by_block(corpus):
	"""trying to make sense of lilo's tweets"""

	f = open(corpus)

	text_block = f.read()
	stripped_block = text_block.strip()
	split_block = stripped_block.split()
	
	return split_block

	f.close()
	

def main():
	args = sys.argv

	input_text, mode = args[1], args[2]

	if mode == "byline":
		print open_and_read_file(input_text)
	elif mode == "byblock":
		print open_and_read_by_block(input_text)
	
	
if __name__ == "__main__":
	main()