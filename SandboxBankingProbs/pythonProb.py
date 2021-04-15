# Problems #1 & #2 from Sandbox Banking Python Code Challenge

import csv
with open('people.csv', 'r') as csvfile:
    ppl_reader = csv.reader(csvfile, delimiter=',')
    