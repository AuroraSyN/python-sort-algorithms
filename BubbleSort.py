#################################################################
#   Neha Gupta
#   Bubble Sort algorithm implementation
#   Google Jump
#   Under direction of Laura Beth Lincoln
#   Explanation found at http://en.wikipedia.org/wiki/Bubble_sort
##################################################################

def Bubblesort(array):
    if type(array) != list:
        return "Input type must be a list"
    if len(array) < 2:
        return array

    length = len(array)
    index1 = 0
    index2 = 1
    swapped = False
    try:
        while(True):
            if array[index1] > array[index2]:
                temp = array[index1]
                array[index1] = array[index2]
                array[index2] = temp
                swapped = True

            index1 += 1
            index2 += 1

            if index2 >= len(array):
                index1 = 0
                index2 = 1
                if (swapped == True):
                    swapped = False
                else:
                    return array
    except TypeError:
        return "All items in array must be integers or floats"
