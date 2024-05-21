from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.tag import map_tag

def pos_tagging(text):
    tokens = word_tokenize(text)
    pos_tags_penn = pos_tag(tokens)
    pos_tags_universal = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in pos_tags_penn]

    return pos_tags_penn, pos_tags_universal

text = input("Enter text for POS tagging: ")

pos_tags_penn, pos_tags_universal = pos_tagging(text)

print("\nPOS tags with Penn Treebank tagset:")
for word, tag in pos_tags_penn:
    print(f"{word}: {tag}")

print("\nPOS tags with Universal tagset:")
for word, tag in pos_tags_universal:
    print(f"{word}: {tag}")

