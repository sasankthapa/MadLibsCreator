import nltk, random
import os,sys
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def playGame(madlib):
    toreturn=""
    for line in madlib.splitlines():
        line=line.strip()
        sentences=sent_tokenize(line)
        for sentence in sentences:
            if('(' in sentence):
                tag=sentence[sentence.find('(')+1:sentence.find(')')]
                word=input(sentence)
                toreturn=toreturn + sentence.replace('(%s)'%tag,word)+' '
            else:
                toreturn=toreturn+sentence+' '
        toreturn=toreturn+'\n'
    os.system('cls' if os.name=='nt' else 'clear')
    return toreturn
    
def initializeStopWords():
    global stop_words
    stop_words=set(stopwords.words("english"))

tags_data={'NN':"Singular Noun",'NNS':"Plural Noun",'NNP':"Proper Noun (Harrison)",'NNPS':"Plural Proper Noun (Americans)",'JJ':"Adjective",'JJR':"Comparitive Adjective (bigger)",'JJS':"Superlative Adjective (biggest)",'RB':"Adverb",'RBR':"Adverb Compative",'RBS':"Adverb Superlative",'VB':'Verb','VBD':"Verb past tense",'VBG':"Verb Continous",'VBN':"Verb Past",'VBP':"Verb",'VBZ':"Verbs 3rd person (sings, takes)"}
def processTag(tag):
    return tags_data.get(tag)

filename=input("Enter name of file:  ")
initializeStopWords()

if not os.path.isfile(filename):
    print("error filenot found")
    sys.exit(-1)

file=open(filename,'r')
lines=file.readlines()
lines=[line.strip() for line in lines]
madlib=""

for line in lines:
    sentences=sent_tokenize(line)
    for a in sentences:
        choices=[]
        words=word_tokenize(a)
        words=[word for word in words if word not in stop_words]
        tagged=nltk.pos_tag(words)
        for taggedWord in tagged:
            tag=taggedWord[1][:1]
            if(tag=='N' or tag=='V' or  tag=='J' or tag=='R' and tag!='RP'):
                choices.append(taggedWord)
        if(len(choices)==0):
            madlib=madlib+a
            continue
        choice=random.choice(choices)
        madlib=madlib+a.replace(choice[0],'(%s)' %processTag(choice[1]))+' '
    madlib=madlib+'\n'

os.system('cls' if os.name=='nt' else 'clear')
print(playGame(madlib))
