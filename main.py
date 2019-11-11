import nltk
import os,sys

filename=input("Enter name of file:  ")

if not os.path.isfile(filename):
    print("error filenot found")
    sys.exit(-1)

file=open(filename,'r')
lines=file.readlines()
lines=[line.strip() for line in lines]
print(lines)