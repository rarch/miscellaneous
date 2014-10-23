#!/usr/bin/env python

import os, sys, getopt

def cycle(n):
    """if even, divide by 2; if odd, triple and add 1; from i to j"""
    count=1
    while n != 1:
        n = 3*n+1 if n%2 else n/2
        count+=1
    return count

def maxcycle(i,j):
    """gets the maximum cycle between 2 end points inclusive"""
    maxc=0

    if i>j:
        i,j = j,i

    for n in xrange(i,j+1):
        temp=cycle(n)
        if temp>maxc:
            maxc=temp
    return maxc
    
def main(argv):
    inputfile=''
    try:
        opts,args=getopt.getopt(argv,"hi:",["infile="])
    except getopt.GetoptError:
        print 'cycle3n1.py -i inputfile'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'cycle3n1.py -i inputfile'
            sys.exit()
        elif opt in ("-i","--infile"):
            inputfile=os.path.abspath(arg)

    if inputfile:
        lines=file(inputfile,"r").readlines()
    else:
        lines=sys.stdin.readlines()
        print "Please wait..."

    for line in lines:
        try:
            (i,j)=map(int,line.split())
            print i, j, maxcycle(i,j)
        except:
            pass

if __name__ == '__main__':
  main(sys.argv[1:])    
