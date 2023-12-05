#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence != '':
        first_chr = sentence[0]
    else:
        first_chr = None
    return (len(sentence), first_char)
