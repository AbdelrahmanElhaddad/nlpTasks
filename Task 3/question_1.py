import spacy
de_nlp = spacy.load('de_core_news_sm')

text = input("Enter your german sentences:\n")

text_doc = de_nlp(text)

text_sent = [sentence.text for sentence in text_doc.sents]

print(text_sent)