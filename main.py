import nltk, random
import os,sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def initializeStopWords():
    global stop_words
    stop_words=set(stopwords.words("english"))

tags_data={'NN':"Singular Noun",'NNS':"Plural Noun",'NNP':"Proper Noun (Harrison)",'NNPS':"Plural Proper Noun (Americans)",'JJ':"Adjective",'JJR':"Comparitive Adjective (bigger)",'JJS':"Superlative Adjective (biggest)",'RB':"Adverb",'RBR':"Adverb Compative",'RBS':"Adverb Superlative",'VB':'Verb','VBD':"Verb past tense",'VBG':"Verb Continous",'VBN':"Verb Past",'VBP':"Verb",'VBZ':"Verbs 3rd person (sings, takes)"}
def processTag(tag):
    return tags_data.get(tag)

filename=input("Enter name of file:  ")
initializeStopWords()
print(stop_words)

if not os.path.isfile(filename):
    print("error filenot found")
    sys.exit(-1)

file=open(filename,'r')
lines=file.readlines()
lines=[line.strip() for line in lines]

for line in lines:
    print(line)
    x=sent_tokenize(line)
    for a in x:
        choices=[]
        words=word_tokenize(a)
        words=[word for word in words if word not in stop_words]
        tagged=nltk.pos_tag(words)
        for taggedWord in tagged:
            tag=taggedWord[1][:1]
            if(tag=='N' or tag=='V' or  tag=='J' or tag=='R' and tag!='RP'):
                choices.append(taggedWord)
        print("x",choices)
    if(len(choices)==0):
        continue
    choice=random.choice(choices)
    print(choice)
    print("y",processTag(choice[1]))
