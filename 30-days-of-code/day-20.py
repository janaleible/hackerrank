#!/bin/python3

import sys

_ = input()
array = list(map(int, input().strip().split(' ')))

def bubble_sort(array: []):
    
    total_swaps = 0
    
    for i in range(len(array)):
        
        iteration_swaps = 0
        
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                
                iteration_swaps += 1
                total_swaps += 1
        
        if iteration_swaps == 0: break
        
    return array, total_swaps

sorted_array, total_swaps = bubble_sort(array)

print('Array is sorted in {} swaps.'.format(total_swaps))
print('First Element: {}'.format(sorted_array[0]))
print('Last Element: {}'.format(sorted_array[-1]))
