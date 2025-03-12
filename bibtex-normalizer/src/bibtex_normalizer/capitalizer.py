import re
from typing import List

from .config import DEFAULT_EXCLUDED_WORDS


def dynamic_bounding_pattern(left: str, right: str) -> str:
    return rf'^\s*{re.escape(left)}(.*){re.escape(right)}\s*$'

def capitalize_title(title: str, excluded_words: List[str] = DEFAULT_EXCLUDED_WORDS) -> str:
    words = title.split()
    capitalized = []
    
    for i, word in enumerate(words):
        if "{" in word:
            capitalized.append(word)
        elif word_has_capital(word) or (i > 0 and word[0].isupper()):
            capitalized.append(f"{{{word}}}")
        elif word.lower() not in excluded_words or i == 0:
            capitalized.append(format_word(word))
        else:
            capitalized.append(word)
    
    return ' '.join(capitalized)

def word_has_capital(word: str) -> bool:
    return any(c.isupper() for c in word)

def format_word(word: str) -> str:
    if '-' in word:
        return "{" + "-".join(w.capitalize() for w in word.split('-')) + "}"
    return "{" + word.capitalize() + "}"
