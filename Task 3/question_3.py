from nltk.corpus import stopwords

languages = ['english', 'german', 'arabic']
stop_words_dict = {}

for lang in languages:
    stop_words_dict[lang] = stopwords.words(lang)
    print(f"Stop words in {lang}:")
    print(stop_words_dict[lang])
    print("\n")

