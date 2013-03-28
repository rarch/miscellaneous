#!/usr/bin/env python
# FizzBuzz from lo to hi inclusive
def FizzBuzz(lo, hi):
    for i in xrange(lo,hi+1):
        out=''
        if i%3==0:
            out=out+'Fizz'
        if i%5 == 0:
            out=out+'Buzz'
        print i if out=='' else out

if __name__ == "__main__":
    FizzBuzz(1,100) # choose 1, 100
