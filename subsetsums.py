#!/usr/bin/env python

# I HAVE 7 BOXES, 35 BALLS, AND EACH BOX HOLDS 1-10 INDISTINCT BALLS. HOW MANY WAYS DOES IT WORK?
# BOX ORDER MATTERS

# ALL SUBSET SUMS OF NUMBERS 1-10 TO 35, REMOVE SUBSETS WITH EMPTY BOXES AND GIVE ALL PERMUTATIONS
# PROBLEM IS NP

BOXES = 7
TOTAL = 35
LIMIT = 10

def countSubsetSums(target,mySet,mySum,termsLeft):
    """count subset sums of given length from sorted set\
        equal to target for current sum and termsLeft"""
    if (termsLeft*mySet[-1]<target-mySum) or \
        (termsLeft*mySet[0]>target-mySum): # cannot possibly achieve subset sum
        return 0            #   with current subsubset (not enough terms or too many)
    if termsLeft==0:        # no more terms
        if mySum==target:   # achieved subset sum
            return 1        # so increment number of solutions
        else:               # failed to achieve subset sum
            return 0        # so dont increment number of solutions
    numSubsetSums=0         # find number of solutions given current beginning
    for choice in mySet:    # add each choice and recurse
        # same target and set of options, new sum, one less term
        numSubsetSums+=countSubsetSums(target,mySet,mySum+choice,termsLeft-1)
    return numSubsetSums

choices = [val+1 for val in xrange(LIMIT)]
numSubsetSums = 0
for choice in choices:
    numSubsetSums+=countSubsetSums(TOTAL,choices,choice,BOXES-1)
print numSubsetSums