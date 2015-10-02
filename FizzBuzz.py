#!/usr/bin/env python
# FizzBuzz from lo to hi inclusive

def FizzBuzz_list(hi,lo=1):
    print '\n'.join(map((lambda e:'FizzBuzz' if not(e%15) else 'Fizz' if not (e%3) else 'Buzz' if not (e%5) else str(e)),
        [i for i in xrange(lo,hi+1)]))

def FizzBuzz(hi,lo=1):
    for i in xrange(lo,hi+1):
        out='' if i%3 else 'Fizz'
        out=out if i%5 else out+'Buzz'
        print out if out else i

def lazyFizzBuzz(lim):
    from itertools import cycle, izip, count, islice

    fizzes = cycle([""]*2 + ["Fizz"])
    buzzes = cycle([""]*4 + ["Buzz"])
    both = (f+b for f,b in izip(fizzes,buzzes))
    fizzbuzz = (word or n for word, n in izip(both, count(1)))

    for i in islice(fizzbuzz,lim):
        print i

if __name__ == "__main__":
    # FizzBuzz(100)
    FizzBuzz_list(100) # choose 1, 100
    # lazyFizzBuzz(100)