import csv
import re
import string
import pickle
import random 

### Train a markov chain with data formatted in a csv from twitter###
def train_chain_twitter(file_name, chain_name):
    tweets = open(file_name, 'r')
    reader = csv.DictReader(tweets)
    markov_chain = {"___start___":{"___count___":0}}
    for row in reader:
        words = row['text'].split()
        for i in range(len(words)):
            #if end of sentence
            if i == len(words) - 1: 
                if words[i] in markov_chain:
                    if "___end___" in markov_chain[words[i]]:
                        markov_chain[words[i]]["___end___"] +=1
                    else:
                        markov_chain[words[i]]["___end___"] = 1
                    markov_chain[words[i]]["___count___"] += 1
                else:
                    markov_chain[words[i]] = {"___end___":1, "___count___":1}
            #if start of sentence
            if i == 0:
                if words[i] in markov_chain["___start___"]:
                    markov_chain["___start___"][words[i]] += 1
                else:
                   markov_chain["___start___"][words[i]] = 1
                markov_chain["___start___"]["___count___"] += 1
            else:
                if words[i-1] not in markov_chain:
                    markov_chain[words[i-1]] = {"___count___":0}
                if words[i] in markov_chain[words[i-1]]:
                    markov_chain[words[i-1]][words[i]] += 1
                else:
                    markov_chain[words[i-1]][words[i]] = 1
                markov_chain[words[i-1]]["___count___"] += 1
    print markov_chain
    chain_file = open(chain_name, 'w')
    pickle.dump(markov_chain, chain_file)
    return markov_chain
    print "file dumped"


### Train a markov chain with each line being a different "tweet"
def train_chain_lines(file_name, chain_name):
    lines = open(file_name, 'r')
    markov_chain = {"___start___":{"___count___":0}}
    for row in lines:
        words = row.split()
        for i in range(len(words)):
            #if end of sentence
            if i == len(words) - 1: 
                if words[i] in markov_chain:
                    if "___end___" in markov_chain[words[i]]:
                        markov_chain[words[i]]["___end___"] +=1
                    else:
                        markov_chain[words[i]]["___end___"] = 1
                    markov_chain[words[i]]["___count___"] += 1
                else:
                    markov_chain[words[i]] = {"___end___":1, "___count___":1}
            #if start of sentence
            if i == 0:
                if words[i] in markov_chain["___start___"]:
                    markov_chain["___start___"][words[i]] += 1
                else:
                   markov_chain["___start___"][words[i]] = 1
                markov_chain["___start___"]["___count___"] += 1
            else:
                if words[i-1] not in markov_chain:
                    markov_chain[words[i-1]] = {"___count___":0}
                if words[i] in markov_chain[words[i-1]]:
                    markov_chain[words[i-1]][words[i]] += 1
                else:
                    markov_chain[words[i-1]][words[i]] = 1
                markov_chain[words[i-1]]["___count___"] += 1
    print markov_chain
    chain_file = open(chain_name, 'w')
    pickle.dump(markov_chain, chain_file)
    return markov_chain
    print "file dumped"

def make_tweet(markov_chain, max_lenght=140):
    word = "___start___"
    sentence = ""
    while True:
        #count is used to help with random word choice
        count = markov_chain[word]["___count___"]
        cont_count = 0
        #random choose a word
        random_count = random.randint(1, count)
        #go though all the words until our random word is found
        for next_word in markov_chain[word]:
            #start random number count
            #disallow ___count___
            if next_word != "___count___":
                cont_count += markov_chain[word][next_word]
                if cont_count >= random_count:
                    if next_word == "___end___":
                        return sentence[1:]
                    sentence += " " + next_word
                    if len(sentence) > max_lenght:
                        return sentence[1:]
                    word = next_word
                    break

if __name__ == '__main__':
    rick_chain = train_chain_lines("Rick/ricks_lines.txt", "rick_chain.pickel")
    make_tweet(rick_chain)
