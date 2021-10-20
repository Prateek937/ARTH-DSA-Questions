'''
Search For Range :

Write a function that takes in a sorted array of integers as well as a target integer.
The function should use a variation of the binary search algorithm to find a range of indices in between which the target number is contained in the array and should return  this range in the form of an array

The first number in the output array should represent the first index at which the target number is located, while the second number should represent the last index at which the target number is located. The function should return [ -1, -1 ] if the integer is not contained in the array


Sample Input :
array = [ 0 ,1,21,33,45,45,45,45,45,45,61,71,73]
target = 45

Sample Output :
[ 4 , 9 ]

'''

def search_range(l, target):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if target > l[mid]:
            start = mid + 1
        elif target < l[mid]:
            end = mid -1
        elif target == l[mid]:
            begin = mid
            term = mid
            while target == l[begin]:
                begin -= 1
            while target == l[term]:
                term += 1
            return [begin+1, term-1]
    return [-1, -1]            

print(search_range([0 ,1,21,33,33,45,45,45,45,45,61,71,73], 45))