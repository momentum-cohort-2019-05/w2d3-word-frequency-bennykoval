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
    ls_text = (str(text)).split(" ")
    return ls_text

def block_words(word_list):
    """Delete overly common link words"""
    new_list = []
    for word in word_list:
        if word not in stop_words:
            new_list.append(word)
    return new_list

def get_dict(word_list):
    word_dict = {}
    for word in word_list:
        if word_dict.get(word) == None:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    cleanest_text = clean_text(file)
    split_ls = split_text(cleanest_text)
    block_ls = block_words(split_ls)
    word_freq = get_dict(block_ls)
    return word_freq

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
    word_freq = print_word_freq(chosen_file.read())
    print(word_freq)