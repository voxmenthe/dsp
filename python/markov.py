#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import sys
import random

filename = sys.argv[1]
numwords = int(sys.argv[2])
#ngramlen = sys.argv[3]

# clean the text
def cleanText(textdump):
    import string

    textdump = str(textdump)

    # remove non-ascii characters
    textdump = ''.join([i if ord(i) < 128 else ' ' for i in textdump])

    # add space after periods
    textdump = string.replace(textdump, '.', '. ')
    textdump = string.replace(textdump, 'Getty', '')
    textdump = string.replace(textdump, '/POLITICO', '')
    textdump = string.replace(textdump, 'AP Photo', '')
    
    return textdump

# create dictionary with follow-on words for n-grams
# input is block of text, and length of the n-gram used
# to work out the distribution
def getNgramDist(text,n=1):
    # return {ngram: {followon word: counts), ...} from corpus text.
    result = {}
    spltext = text.split()
    if n < 1:
        raiseValueError('n must be greater than 1')
    for i in range(len(spltext)):
        if i + n + 1 < len(spltext):
            words = spltext[i:i+n+1]
            ngram = ' '.join(words[:-1])
            followon = words[-1]
            if ngram in result:
                if followon in result[ngram]:
                    result[ngram][followon] += 1
                else:
                    result[ngram][followon] = 1
            else:
                result[ngram] = {}
                result[ngram][followon] = 1                    
    return result

# generate string of markov text taking distribution
# dictionary and length of output text in words
# as inputs
def markov_text(dictionary, nwords):
    import numpy as np
    nwords = int(nwords)
    # set the ngram length based on
    # the length of ngram in the dictionary:
    ngramlen = len(dictionary.keys()[0].split())
    
    result = ""
    if nwords < 1:
        raise ValueError('nwords must be greater than 1.')
    else:
        result = random.choice(dictionary.keys())
        nwords -= ngramlen
        for i in range(nwords):
            
            # take the last n words and turn them into current key:
            if ngramlen == 1:
                key = "".join(result.split()[-ngramlen:])
            else:
                key = " ".join(result.split()[-ngramlen:])
            
            #key = result.split()[-1]
            
            # create array of follow-on words 
            words = dictionary[key].keys()
            # get matching probabilities
            matchprobs = []
            for word in words:
                matchprobs.append(dictionary[key][word])
            
            # put the probabilities for follow-on words in transition matrix
            probs = np.array(matchprobs,dtype=np.float32)
            probs /= probs.sum()

            # choose the next word based on the transition matrix
            newword = np.random.choice(words,p=probs)

            result += ' ' + newword
    return result

# load saved text from file
with open(filename, "r") as imported:
    alltext = imported.read()
    imported.close()

# clean the text
cleanedtext = cleanText(alltext)

# getting the distribution of words
dictionary = getNgramDist(cleanedtext,n=2)

# generate the text
newtext = markov_text(dictionary, numwords)

print(newtext)