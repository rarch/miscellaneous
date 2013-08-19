#!/usr/bin/env python
import random
import array

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile):
        if random.randrange(num + 2):
            continue
        line = aline
    return line

def main():
    word=""

    while word == '' or ' ' in word: # get word
        word=random.choice(list(open('words.txt'))).strip()

    obscured = array.array('c')
    i=0

    while i<len(word):
        obscured.append("-")
        i+=1

    lives=5
    done=[]

    playing=True
    while playing:
        print "\nWord is:", obscured.tostring()
        print "Lives remaining:", lives
        guess = raw_input("Enter guess:") # get input
        guess = guess.replace("\n", "") #remove carriage returns

        if guess not in done: #check for already guessed
            if guess in word: #check if char is present
                i=0
                lastval=0
                while i < word.count(guess):
                   obscured[word.index(guess, lastval)]=guess #replace some -
                   lastval = word.index(guess, lastval) + 1
                   i+=1

                if "-" not in obscured.tostring():
                    print "You guessed the word:", word, ". Lives remaining:", lives
                    playing=False #on solve

            elif guess not in word:
                print guess, "is not in the word!" #not in word
                lives-=1

                if lives == 0:
                    print "You failed to guess the word:", word,"\n" #out of lives
                    playing=False

            done.append(guess) #add guess to already guessed

        elif guess in done:
            print guess, "already tried!" #if already done print so

if __name__=="__main__":
    main()