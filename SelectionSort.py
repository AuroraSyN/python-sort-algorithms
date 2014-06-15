##################################################################
#   Neha Gupta
#   Selection Sort algorithm implementation
#   Google Jump
#   Under direction of Laura Beth Lincoln
#   Reference, explanation and C++ code found in
#   "Programming Interviews Exposed" (Mongan et al)
##################################################################

def Selectionsort(array):
    '''Sorts a given array with selection sort algorithm'''
    if type(array) != list:
        return
    #TODO: check that all items in array are int/double

    return selectionSortRecursive(array, 0)

def selectionSortRecursive(array, start):
    '''Sorts a subset of the array starting at a specified index, start'''
    if (start < len(array)-1):

        #Code to find the position of a minimum value starting at start
        minPos = start
        for i in range(start, len(array)):
            if (array[i] < array[minPos]):
                minPos = i

        #Swaps 2 elements in the array
        if (minPos != start):
            temp = array[start]
            array[start] = array[minPos]
            array[minPos] = temp

        selectionSortRecursive(array, start+1)

    return array
            

        
    
