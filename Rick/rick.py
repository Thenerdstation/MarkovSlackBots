#!/usr/bin/env python
# encoding: utf-8

import string
import pickle
import random 
from Markov.markov_chains import make_tweet
import os
global rick_file_name, rick_file

file_name = 'rick_chain.pickel'
file_path = os.path.join(os.path.dirname(file_name))
file = open(file_path, "r")

def morty():
    markov_chain = pickle.load(file)
    return make_tweet(markov_chain)

if __name__ == '__main__':
    #pass in the username of the account you want to download
    #get_all_tweets("realDonaldTrump")
    #trump_chain = train_chain("realDonaldTrump_tweets.csv")
    markov_chain = pickle.load(file)
    print make_tweet(markov_chain)