#!/usr/bin/env python3

import math

def formula(tab, abscissa, ord, i, X):
    res = (- tab[i - 1] / 30 * pow(X - abscissa[i], 3) + tab[i] / 30 * pow(X - abscissa[i - 1], 3)
            - (ord[i - 1] / 5 - 5 / 6 * tab[i - 1]) * (X - abscissa[i]) + (ord[i] / 5 - 5 / 6 * tab[i])
            * (X - abscissa[i - 1]))
    return(res)


def mathindex(rad, tab, ord, abscissa, answer):
        A = 6 * (rad['r10'] - 2 * rad['r5'] + rad['r0']) / 50
        B = 6 * (rad['r15'] - 2 * rad['r10'] + rad['r5']) / 50
        C = 6 * (rad['r20'] - 2 * rad['r15'] + rad['r10']) / 50
        tab[2] = (B - (A + C) / 4) * 4 / 7
        tab[1] = A / 2 - 0.25 * tab[2]
        tab[3] = C / 2 - 0.25 * tab[2]
        for d in range(int(rad['n'])):
            X = 20 / (rad['n'] - 1) * d
            i = int((X - 0.01) / 5) + 1
            res = formula(tab, abscissa, ord, i, X)
            answer.append(res)


def display(tab, rad, answer):
        print("vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(
            tab[0] if round(tab[0], 1) != 0 else 0,
            tab[1] if round(tab[1], 1) != 0 else 0,
            tab[2] if round(tab[2], 1) != 0 else 0,
            tab[3] if round(tab[3], 1) != 0 else 0,
            tab[4] if round(tab[4], 1) != 0 else 0))
        for i in range(int(rad['n'])):
            print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(
                20 / (rad['n'] - 1) * i, answer[i]))
