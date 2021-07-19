from typing import List
import MeCab
from .ignore_words import ignore_words


def get_words_from_sentence(sentence: str) -> List[str]:
    """
    Take a sentence and get the unique words (i.e. dictionary form)
    """
    tagger = MeCab.Tagger()
    sentence_no_parantheses = remove_ignore_words(sentence)
    node = tagger.parseToNode(sentence_no_parantheses)
    unique_words = set()

    while node:
        feature = node.feature.split(",")
        if len(feature) > 10 and feature[10] not in ignore_words:
            unique_words.add(feature[10])
        node = node.next
    return list(unique_words)


def remove_ignore_words(sentence: str) -> str:
    result = []

    for char in sentence:
        if char not in ignore_words:
            result.append(char)

    return "".join(result)
