from nltk.tokenize import word_tokenize, sent_tokenize

text = input("Input: ")
type_of_tokenization = int(input("Word[0] or Sentence[1] tokenizaiton? "))

if type_of_tokenization == 1:
    print(sent_tokenize(text))
elif type_of_tokenization == 0:
    print(word_tokenize(text))
else:
    print("You entered some wrong answer for tokenization type, please restart and try again.")