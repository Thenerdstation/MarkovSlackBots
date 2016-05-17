#!/usr/bin/env python
# encoding: utf-8

import string
import pickle
import random 
from Markov.markov_chains import make_tweet
import os

### File path of your pickle ###
file_name = 'Rick/rick_chain.pickle'


global markov_chain
file_path = os.path.join(os.path.realpath(file_name))
file = open(file_path, "r")
markov_chain = pickle.load(file)

def morty():
    return make_tweet(markov_chain)

if __name__ == '__main__':
    #print a tweet for debugging
    print make_tweet(markov_chain)
