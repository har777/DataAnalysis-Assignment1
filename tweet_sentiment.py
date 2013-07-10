import sys
import json
import re

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    scores = {} # the sentiments and scores are stored in this dictionary
    for line in sent_file:
        term, score  = line.split("\t")  
        scores[term] = int(score)  

    tweets = []
    for line in tweet_file:
        tweet_lines = json.loads(line)
        if "text" in tweet_lines.keys():
            tweets.append(tweet_lines["text"].encode('utf-8'))
    
    
                          
    for tweet in tweets:
        
        tweet_score = 0
        tweet_words = re.findall(r"[\w]+", tweet)

        for word in tweet_words:
            word_score = scores[word.lower()] if word.lower() in scores else 0
            tweet_score += word_score

        
        print float(tweet_score)
            


if __name__ == '__main__':
    main()
