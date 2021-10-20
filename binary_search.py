# For running python with test cases
# $ python3 -m unittest binary_search.py

'''
Binary Search :
Write a function that takes in a sorted array of integers as well as target integer.
The function should use binary search algo to determine if the target integer is contained in the array and should return its index if it is, otherwise -1

Sample Input:
array = [ 0, 1, 21, 33, 45,45,61,71, 72, 73 ]
target = 33

Sample Output:
3
'''

import unittest

def binary_search(l, target):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start+end)//2
        if target > l[mid]:
            start = mid + 1
        elif target < l[mid]:
            end = mid - 1
        elif target == l[mid]:
            return mid
        
    return -1


class Test(unittest.TestCase):
    def test_binary_search(self):
        l = [[1,2,3,4], [2, 3, 4, 5, 5, 62], [2, 2, 3, 4, 6, 63],[0, 1, 21, 33, 45, 45, 61, 71]]
        target = [1,62,6,22]
        result = [0, 5, 4, -1]
        for i in range(len(l)):
            elem_index = binary_search(l[i], target[i])
            self.assertEqual(elem_index, result[i])
            print(target[i],"at index : ", elem_index)
            
            






