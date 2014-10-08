#!/usr/bin/env python

import sys


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(corpus)
    text_block = f.read()
    stripped_block = text_block.strip()
    
    punctuation = ['$', '%', '&', '(', ')', '*', '+', '/', '<', '=', '>', '@', '[', ']', '^', '`', '{', '|', '}', '~', '_']
   
    block_no_punctuation = ""
    
    # print stripped_block
    for character in stripped_block:
        if character not in punctuation:
            block_no_punctuation += character

    split_block = block_no_punctuation.split()

    # return split_block

    markov_dictionary = {}

    for i in range(len(split_block) -2):

        dictionary_key = (split_block[i], split_block[i+1])
        dictionary_value = split_block[i + 2]

        if dictionary_key not in markov_dictionary.keys():
            markov_dictionary[dictionary_key] = [dictionary_value]
        else:
            markov_dictionary[dictionary_key].append(dictionary_value)

    return markov_dictionary 



    # return {}
    # print split_block

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    return "Here's some random text."

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text
    print chain_dict

if __name__ == "__main__":
    main()
