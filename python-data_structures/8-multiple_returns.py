#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_c = None
    else:
        first_c = sentence[0]
    return (len(sentence), first_c)
