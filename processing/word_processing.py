import nltk
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
nltk.download("stopwords")
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer



example_string = """
    Muad'Dib learned rapidly because his first training was in how to learn.
    And the first lesson of all was the basic trust that he could learn.
    It's shocking to find how many people do not believe they can learn,
    and how many more believe learning to be difficult."""
print(sent_tokenize(example_string))

def get_most_repeated_word(word:str):
    pass


def filter_words(string:str):
    stop_words = set(stopwords.words("english"))
    list_of_words = word_tokenize(string)
    filtered_words = []
    for word in list_of_words:
        if word.casefold() not in stop_words:
            filtered_words.append(word)
    return filtered_words


def stemming_word(string: str):
    stemmer = PorterStemmer()
    words = word_tokenize(string)
    return [stemmer.stem(word) for word in words]


def word_tags(string: str):
    words = word_tokenize(string)
    return nltk.pos_tag(words)


def word_lemmanting(string: str):
    lemmatizer = WordNetLemmatizer()
    words = word_tokenize(string)
    return [lemmatizer.lemmatize(word) for word in words]


def word_chunking(string: str):
    words =  word_tokenize(string)
    nltk.download("averaged_perceptron_tagger")
    tokenized_words = nltk.pos_tag(words)
