#!/usr/bin/python3
# eturns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    if sentence != '':
        return (len(sentence), sentence[0] if len(sentence) > 0 else None)
