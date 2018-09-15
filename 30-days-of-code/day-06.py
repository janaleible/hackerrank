number_of_cases = int(input())

for case in range(number_of_cases):
    string = input()
    odd = ''
    even = ''

    for index, char in enumerate(string):
        if index % 2 == 0:
            even = even + char
        else:
            odd = odd + char

    print(even + ' ' + odd)