STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import re

def clean_text(text):
    """Purge text of casing, special characters"""
    text = (str(text)).lower()
    text = re.sub(r'[^a-z ]', '', text)
    text = re.sub('\\n', '', text)
    return text

def split_text(text):
    """Split string into words"""
    text = (str(text)).split(" ")
    return text

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    clean_text(file)
    split_text(file)
    return

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)

with open(file) as chosen_file:
    #print_word_freq(chosen_file.readline())
    print(repr(chosen_file.readline()))
    #with open(file) as source_file:
    #source_str = source_file.read