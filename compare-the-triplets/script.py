#!/bin/python3

import math
import os
import random
import re
import sys


def award_points(self, other):
    return sum([ratings[0] > ratings[1] for ratings in zip(self, other)])


def compareTriplets(a, b):
    points_alice = award_points(a, b)
    points_bob = award_points(b, a)

    return points_alice, points_bob


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ratings_alice = list(map(int, input().rstrip().split()))

    ratings_bob = list(map(int, input().rstrip().split()))

    result = compareTriplets(ratings_alice, ratings_bob)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()