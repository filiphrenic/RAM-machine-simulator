#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulator for a simple RAM and Macro machine
Author: Filip Hrenić
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

    num_exec = 0 # number of executed commands

    c_idx = 1
    while c_idx <= num_c:

        num_exec += 1

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
            if R[x]:
                R[x] -= 1
            else:
                c_idx = m

        elif c[0] == 'GOTO':
            m = int(c[1])
            c_idx = m

        elif c[0] == 'ZERO':
            x = int(c[1])
            ensure_index(R,x)
            R[x] = 0

        elif c[0] == 'MOVE':
            x = int(c[1])
            y = int(c[2])
            # x should exist so no need for ensure_index
            ensure_index(R,y)
            R[y] = R[x]

        else: # STOP
            break

    print 'Number of executed commands = %d' % num_exec
    print 'Result = %d' % R[0]

if __name__ == '__main__':
    main()
