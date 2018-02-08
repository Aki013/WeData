import json
import os
import sys

# Add lins directory to module search path "libs"
parent_dir = os.path.abspath(os.path.dirname(__file__))
libs_dir = os.path.join(parent_dir, 'libs')
sys.path.append(libs_dir)

# Now you can import any library located in the "libs" folder !
from textblob.classifiers import NaiveBayesClassifier
import nltk

fp = open('.\Classifiers\classifier_fr.json', 'r')

#python -m textblob.download_corpora
cl = NaiveBayesClassifier(fp, format="json")


print(cl.classify("mauvais"))

