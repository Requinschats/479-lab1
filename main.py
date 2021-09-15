from nltk.corpus import reuters
from nltk import word_tokenize
from constants import PREPOSITIONS

def main():
    sampleText = reuters.raw('training/9920')
    sampleTextTokenized = word_tokenize(sampleText)

    presenceDictionary = {}
    for token in sampleTextTokenized:
        lowerCaseToken = token.lower()
        if not PREPOSITIONS.get(lowerCaseToken):
            presenceDictionary[token] = "true"
    print(len(presenceDictionary))


if __name__ == '__main__':
    main()
