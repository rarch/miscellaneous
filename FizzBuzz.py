#!/usr/bin/env python
# FizzBuzz from lo to hi inclusive
# def FizzBuzz(lo, hi):
#     for i in xrange(lo,hi+1):
#         out=''
#         if i%3==0:
#             out=out+'Fizz'
#         if i%5 == 0:
#             out=out+'Buzz'
#         print i if out=='' else out

def FizzBuzz(lo, hi):
    # print map((lambda e:'FizzBuzz' if not(e%15) else 'Fizz' if not (e%3) else 'Buzz' if not (e%5) else e),
    #     [i for i in xrange(lo,hi+1)])

    # for i in xrange(lo,hi+1):
    #     out=''
    #     if i%3==0:
    #         out=out+'Fizz'
    #     if i%5 == 0:
    #         out=out+'Buzz'
    #     print i if out=='' else out

    for i in xrange(lo,hi+1):
        out='' if i%3 else 'Fizz'
        out=out if i%5 else out+'Buzz'
        print out if out else i


if __name__ == "__main__":
    FizzBuzz(1,100) # choose 1, 100
