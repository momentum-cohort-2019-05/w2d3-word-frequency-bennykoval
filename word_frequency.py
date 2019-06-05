STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

#import re

#def split_string(file):
    #"""Read in `file` and split strings in that file."""

#def print_word_freq(file):
    #"""Read in `file` and print out the frequency of words in that file."""
    #pass

#with open(file) as chosen_file:
   # for line in f:
    #string_split = line.split()
    #print(repr(file.readline()))
    #len(chosen_file.readline())

with open(file) as chosen_file:
    chosen_file = print(repr(file.readline()))

#with open('flights.txt', 'r') as f:
    #for line in f:
        #y = line.split()
        #print(y)

#if __name__ == "__main__":
    #import argparse
    #from pathlib import Path

    #parser = argparse.ArgumentParser(
        #description='Get the word frequency in a text file.')
    #parser.add_argument('file', help='file to read')
    #args = parser.parse_args()

    #file = Path(args.file)
    #if file.is_file():
        #print_word_freq(file)
    #else:
        #print(f"{file} does not exist!")
        #exit(1)
