# -*- coding: utf-8 -*-
__author__ = 'billz'


"""
Compute the Damerau-Levenshtein distance between two given
strings (s1 and s2)
"""
def EditDistance(s1, s2):
    d = {}
    s1 = unicode(s1)
    s2 = unicode(s2)
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1 #init the table when str2 is a empty string
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1 #init the table when str1 is a empty string

    for i in xrange(0,lenstr1):
        for j in xrange(0,lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i>1 and j>1 and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition

    return d[lenstr1-1,lenstr2-1]

while True:
    print "中文Edit Distance (enter a string; enter exit to quit)"
    userStr = raw_input("Enter a string: ")

    if userStr == "exit": break
    str2 = raw_input("Enter 2nd str: ")

    print "editDistance() = ", EditDistance(userStr, str2)
