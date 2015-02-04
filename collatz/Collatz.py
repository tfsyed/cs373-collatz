#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

import math 
def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

CollatzCache = {}

 
 
def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    assert i > 0
    assert i < 1000000
    assert j > 0
    assert j < 1000000

    #introducing low and high as the inclusion and exclusion range variables.
    if(i < j):
        low = i
        high = j
    elif( i < j/2):
        low = j/2
        high = j
    else:
        low = j
        high = i

    maxLength = 1

    for x in range(low,high+1):
        cycle_length = 1
      #  print('cycle length is' + str(cycle_length) + '\n')
        if (x == 1):
            CollatzCache[x] = cycle_length
        while(x> 1):
            if x in CollatzCache:
                cycle_length += CollatzCache[x]-1
            elif(x % 2 == 0):
                x = x >> 1
                cycle_length+=1
            else:
                x = f(x)
                cycle_length+=2
        
        CollatzCache[x] = cycle_length  

        #post condition checks: 
        assert CollatzCache != {} , 'Nothing cached'     

       # print('Inremented cycle length is' + str(cycle_length) + '\n')
        maxLength = max(maxLength,cycle_length)
       # print('Max cycle length is' + str(maxLength) + '\n')
    #invariant check 
    assert maxLength >= cycle_length
    #return value check 
    assert maxLength > 0
    return maxLength
    

def f(n):
    return n + (n >>1) + 1
#--------------
# cycle_length
#--------------

def cycleLength (n):
    assert n > 0
    c = 1
    while n > 1:
        if (n % 2) == 0:
            #n = (n//2)
             n = n >> 1
             c+=1
        else:
            #n = (3 * n)+1
            n = f(n)
            c+=2
        
    assert c >0 
    return c

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
