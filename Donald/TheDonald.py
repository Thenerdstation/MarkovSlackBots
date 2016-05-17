#!/usr/bin/env python
# encoding: utf-8

import string
import pickle
import random 
from Markov.markov_chains import make_tweet


def maga():
    file = open("trump_chain.pickle", "r")
    markov_chain = pickle.load(file)
    return make_tweet(markov_chain)

if __name__ == '__main__':
    #pass in the username of the account you want to download
    #get_all_tweets("realDonaldTrump")
    #trump_chain = train_chain("realDonaldTrump_tweets.csv")
    file = open("./Donald/trump_chain.pickle", "r")
    markov_chain = pickle.load(file)
    print make_tweet(markov_chain)
