import random
import re
import sys
import traceback
import numpy

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

filename = 'bank_transactions.csv'
training_fname = 'training_set.csv'

def read_lines(filename):
    lines = []
    with open(filename) as fd:
        l = fd.readline()
        while l != "":
            if re.match("^\d{4}/\d{2}/\d{2},", l):
                # Only consider line starting with a valid date
                # This allows skipping header, and possible comments
                lines.append(l.strip())
            l = fd.readline()
    return lines

def __init_training_set(training_fname):
    training_set = read_lines(training_fname)
    transactions = [",".join(l.split(',')[:-1]) for l in training_set]
    categories   = [         l.split(',')[-1]   for l in training_set]
    return transactions

read_lines(filename)

transacs = __init_training_set(training_fname)

#print(transacs)

#amount = [(v.split(',')[-1].replace(' ','')) for v in transacs]

amount = sum([float(v.split(',')[-1].replace(' ','')) for v in transacs])

print(amount) 

ln = input("> ").split()

out_fname = ln[1]