#!/usr/bin/env python
# FizzBuzz from lo to hi inclusive

def FizzBuzz_list(lo,hi):
    print '\n'.join(map((lambda e:'FizzBuzz' if not(e%15) else 'Fizz' if not (e%3) else 'Buzz' if not (e%5) else str(e)),
        [i for i in xrange(lo,hi+1)]))

def FizzBuzz(lo, hi):
    for i in xrange(lo,hi+1):
        out='' if i%3 else 'Fizz'
        out=out if i%5 else out+'Buzz'
        print out if out else i

if __name__ == "__main__":
    # FizzBuzz(1,100)
    FizzBuzz_list(1,100) # choose 1, 100
