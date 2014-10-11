#!/usr/bin/env python

import sys
import random
import string

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    f = open(corpus)
    text_block = f.read()
    stripped_block = text_block.strip()
    
    punctuation = ['%', '(', ')', '*', '+', '/', '<', '=', '>', '[', ']', '^', '`', '{', '|', '}', '~', '_']
   
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

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    # return "Here's some random text."

    starters = []
    end_punctuation = ['!', '.', '"', '?']
    # end_tweet = False

    for chain in chains.keys():
        if chain[0][0] in string.ascii_uppercase:
            starters.append(chain)

    start_key = random.choice(starters) # Still stunting,
    value = random.choice(chains[start_key]) # how
    silly_list = str(start_key[0]) + " " + str(start_key[1]) # Still stunting,

    # for i in range(len(chains.keys())):
    #     print start_key
    #     print value

    while start_key in chains.keys() and (len(silly_list) < 140):
        # print "This is our start_key: %s, %s" % (start_key[0], start_key[1])
        # print "This is our value: %s" % value
        # markov_phrase = start_key[0],start_key[1], value,
        # print value
        silly_list = silly_list + " "
        value = random.choice(chains[start_key])
        silly_list = silly_list + str(value)
        start_key = (start_key[1], value)
    
    x = 0
    for mark in end_punctuation:
        if mark not in silly_list:
            x += 1
    if x == len(end_punctuation):
        if len(silly_list) < 140:
            silly_list = silly_list + "."
        else:
            return silly_list

        # print silly_list
    # print silly_list
    # print "silly list[-1] is %r" % (silly_list[-1])
    # print "silly_list[-2] is %r" % (silly_list[-2])

    while silly_list[-1] not in end_punctuation:
        silly_list = silly_list[:-1]
    print silly_list
        # if silly_list[-1] in end_punctuation:
        #     print silly_list

        # if start_key[-1][-1] in end_punctuation:
        #     try
        #         silly_list = silly_list + str(value) + " "
        #         start_key = (start_key[1], value)

        #     except:
        #         len(silly_list) + len(str(value)) > 140
        #         break
        # # else:
        #     silly_list = silly_list + str(value) + " "
        #     start_key = (start_key[1], value)


        # if silly_list[-2] in end_punctuation:
        #     new_key = (start_key[1], value)

            # if (len(silly_list) + len(random.choice(chains[new_key]))) > 140:
            #     break
      
            # new_key = (start_key[1], value)
            # print "New Key is %s %s" % (new_key[0], new_key[1])
            # start_key = new_key


            
        # start_key = new_key
        # silly_list = silly_list + str(value) + " "
        # start_key = (start_key[1], value) # start key s/b stunting, how
        
        # break if the list is already ending in punctuation and adding
        # a new value will make the string longer than 140 characters
        
            
        #     len(silly_list + str(value)) > 140:
        #     break
        # else:
        #     # silly_list = silly_list + str(value) + " "
        #     # new_key = (start_key[1], value) # start key s/b stunting, how
        #     start_key = new_key

        # while len(silly_list) <= 140 and value[-1] not in enders:
        # if len(silly_list) > 140:
        #     break
        # silly_list.append(value,)
        # print start_key

    # print silly_list

def main():
    args = sys.argv

    # Change this to read input_text from a file
    input_text = args[1]

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    # print random_text
    # print chain_dict

if __name__ == "__main__":
    main()
