##################################################################
#   Neha Gupta
#   Quicksort algorithm implementation
#   Google Jump
#   Under direction of Laura Beth Lincoln
#   Translated from CSE 331 MSU Spring 14 Project 1 Assignment
##################################################################

def swap(index, largerIndex, array):
    temp = array[index]
    array[index] = array[largerIndex]
    array[largerIndex] = temp

def quickRecursive(array, leftIndex, rightIndex):
    if (leftIndex < rightIndex):
        pivot = array[rightIndex]
        largerIndex = leftIndex

        for i in range (leftIndex, rightIndex):
            if (array[i] < pivot):
                swap(i, largerIndex, array)
                largerIndex = largerIndex + 1
        swap(rightIndex, largerIndex, array)
        quickRecursive(array, leftIndex, largerIndex -1)
        quickRecursive(array, largerIndex+1, rightIndex)


def Quicksort(array):
    '''
    Quicksort function
    Assumes that the pivot is the first element
    '''
    if type(array) != list:
        return
    #TODO: Error check that everything in the array is an int or float, size 0, size 1
    leftIndex = 0
    rightIndex = len(array) - 1
    quickRecursive(array, leftIndex, rightIndex)
    return array


