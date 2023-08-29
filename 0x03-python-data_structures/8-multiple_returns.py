#!/usr/bin/python3
# Returns a tuple with the length of a string and its first character.
def multiple_returns(sentence):
    return len(sentence), sentence[0] if len(sentence) > 0 else None
