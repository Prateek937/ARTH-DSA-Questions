'''
Index Equals Value :

Write a function that takes in a sorted array of distinct integers and return the first index in the array that is equal to the value at that index. In the others words, your function should return the minimum index where index == array[index]

If there is no such index, your function should return -1

Sample Input
Array = [ -5, -3 , 0 , 3 , 4, 5, 9 ]

Sample Output 
3

'''


def index_equal_value(l):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid > l[mid]:
            start = mid + 1
        elif mid < l[mid]:
            end = mid -1
        elif mid == l[mid]:
            begin = mid
            final = mid
            while begin >= l[begin] and l[begin] >= 0:
                if begin == l[begin]:
                    final = begin
                begin -= 1
            return final
    return -1

print(index_equal_value( [ 0, 1 , 0 , 3 , 4, 5, 9 ]))