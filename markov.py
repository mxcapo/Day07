#!/usr/bin/env python
import random
import sys

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    cinderella_dict = {}
    f = open(corpus)

    story = f.read()
    words = story.strip()
    words = story.split()
    
    # for i in range(len(words) - 2):
    #     dictionary_key_pair = (words[i], words[i + 1])
    #     dictionary_value = words[i+2]
        
    #     if dictionary_key_pair not in cinderella_dict:
    #         cinderella_dict[dictionary_key_pair] = dictionary_value
    #     else:
    #         cinderella_dict[dictionary_key_pair].append(dictionary_value)
    print words
    # print cinderella_dict       
# we made a bunch of lists , oops
def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    
    start_key = random.choice(chains.keys())
    value = random.choice(chains[start_key])
    # print "This is our start key %s, %s" % (start_key[0], start_key[1])
    # print "%s, %s, %s" % (start_key[0], start_key[1], value)
    
    
    while start_key in chains:
        current_key = (start_key[1], value)
        value = random.choice(chains[current_key])
        random_text_string = current_key[0], current_key[1]
        # random_text_string = random_text_string.append(value)
        print random_text_string
        # print "This is our current key %s, %s" % (current_key[0], current_key[1])
        start_key = current_key

        # print "This is our new one: %s, %s, %s" % (start_key[0], start_key[1], str(value))
    #     pass


def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text

if __name__ == "__main__":
    main()
