#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulator for a simple RAM machine
Author: Filip Hrenić

Developed to check homework assignment for college course
Mathematical Logic and Computability

supports only 4 operations:
    - INC x   => increment value in register x by 1
    - DEC x m => decrement value in register x by 1 if it's greater than 0,
                  otherwise go to instruction m
    - GOTO m  => go to instruction m
    - STOP    => stop simulator

first line must contain input arguments, or be empty if it has none
first argument is placed into register 1, second into register 2, ...
every other line must be an operation
commands are indexed from 1

final result should be found in register 0
all registers (that aren't filled with input args) are initialy 0
"""

import sys

def ensure_index(L, n):
    # ensure that accessing L[n] will pass
    L.extend( (0,) * max(n+1-len(L), 0) )

def main():
    if len(sys.argv) == 2:
        reader = open(sys.argv[1], 'r')
    else:
        reader = sys.stdin

    # registers
    R = [int(n) for n in reader.readline().split()]
    R.insert(0, 0) # result

    # commands
    C = [line.strip().split() for line in reader]
    num_c = len(C)

    c_idx = 1
    while c_idx <= num_c:
        c = C[c_idx-1] # commands numbered from 1
        c_idx += 1
        if c[0] == 'INC':
            x = int(c[1])
            ensure_index(R,x)
            R[x] += 1
        elif c[0] == 'DEC':
            x = int(c[1])
            m = int(c[2])
            ensure_index(R,x)
            R[x] -= 1
            c_idx = m
        elif c[0] == 'GOTO':
            m = int(c[1])
            c_idx = m
        else: # STOP
            break

    print 'Result = %d' % R[0]

if __name__ == '__main__':
    main()
