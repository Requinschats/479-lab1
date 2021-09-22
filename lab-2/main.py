import numpy as np
from pathlib import Path


def getBetweenTokens(string, startToken, endToken, endOffset):
    return string[string.find(startToken) + len(startToken): string.find(endToken) - endOffset]


def main():
    fileContent = Path('reuters21578/reut2-021.sgm').read_text()
    documents = np.array(fileContent.split("<REUTERS"))

    documentsIndex = {}

    for document in documents:
        documentId = getBetweenTokens(document, 'NEWID="', '<DATE>', 3)
        documentContent= getBetweenTokens(document, '<BODY>', '</BODY>', 0)
        documentsIndex[documentId] = documentContent

    testId = "21001"
    print(documentsIndex["21001"])

main()
