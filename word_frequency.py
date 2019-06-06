stop_words = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import re

def clean_text(text):
    """Purge text of casing, special characters"""
    str_text = (str(text)).lower()
    str_text = re.sub(r'[^a-z ]', '', str_text)
    str_text = str_text.replace('\n', '')
    return str_text

def split_text(text):
    """Split string into words"""
    text = (str(text)).split(" ")
    return text

def block_words(text):
    """Delete overly common link words"""
    new_list = []
    for i in text:
        if i not in stop_words:
            new_list.append(i)
    return new_list

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    cleanest_text = clean_text(file)
    splittest_text = split_text(cleanest_text)
    blockiest_text = block_words(splittest_text)
    return blockiest_text

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
    blockiest_text = print_word_freq(chosen_file.read())
    print(blockiest_text)