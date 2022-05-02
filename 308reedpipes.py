#!/usr/bin/env python3

import tools
import sys
from sys import argv, exit

def Usage():
        print ("USAGE:\n\t./308reedpipes r0 r5 r10 r15 r20 n\n")
        print ("DESCRIPTION:\n\tr0\tradius (in cm) of pipe at the 0cm abscissa")
        print ("\tr5\tradius (in cm) of pipe at the 5cm abscissa")
        print ("\tr10\tradius (in cm) of pipe at the 10cm abscissa")
        print ("\tr15\tradius (in cm) of pipe at the 15cm abscissa")
        print ("\tr20\tradius (in cm) of pipe at the 20cm abscissa")
        print ("\tn\tnumber of points needed to display the radius")
        exit(0)

 
def starter(rad, ord, args):
    for arg, i in zip(rad, range(1, len(args))):
        try:
            float(args[i])
        except ValueError:
            print("Error detected. Check what you've entered")
            exit(84)
        if float(args[i]) <= 0 :
            print("Only positives values are allowed.")
            exit(84)
        rad[arg] = float(args[i])
        if rad[arg] is not rad['n']:
            ord.append(rad[arg])
    try:
        int(args[6])
    except ValueError:
        print("Last number should be a positive number")
        exit(84)
    if (int(args[6]) <= 1):
        print("Last number should be greater than 1")
        exit(84)

def main():
    answer = []
    ord = []
    abscissa = [0, 5, 10, 15, 20]
    tab = [0, None, None, None, 0]
    rad = {'r0': 0, 'r5': 0, 'r10': 0, 'r15': 0, 'r20': 0, 'n': 0}   
    if len(argv) == 0:
        exit(84)
    if len(argv) == 2 and argv[1] == "-h":
        Usage()
    if len(argv) != 7:
        exit(84)
    starter(rad, ord, argv)
    tools.mathindex(rad, tab, ord, abscissa, answer)
    tools.display(tab, rad, answer)


if __name__ == "__main__":
    main()