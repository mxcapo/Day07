#!/usr/bin/env python

import sys
from sys import argv

script, filename = argv




def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    cinderella_dict = {}
    f = open(corpus)
    i = 0

    for line in f:
        line = line.strip()
        words = line.split() 
        # return words
       
        for i in range(len(words) - 2):
            dictionary_key_pair = (words[i], words[i + 1])
            dictionary_value = [words[i+2]]
            
            if dictionary_key_pair not in cinderella_dict:
                cinderella_dict[dictionary_key_pair] = dictionary_value
            else:
                cinderella_dict[dictionary_key_pair].append(dictionary_value)
        # print words
        return cinderella_dict       

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = filename

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()
