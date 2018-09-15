#!/bin/python3

import re


if __name__ == '__main__':
    N = int(input())

    people_with_gmail = []
    
    for iteration in range(N):
        (firstName, email) = input().split()

        if re.match('.*@gmail\.com', email):
            people_with_gmail.append(firstName)
            
    for name in sorted(people_with_gmail):
        print(name)
