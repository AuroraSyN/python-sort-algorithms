##################################################################
#   Neha Gupta
#   Mergesort algorithm implementation
#   Google Jump
#   Under direction of Laura Beth Lincoln
#   Pseudocode: http://en.wikipedia.org/wiki/Merge_sort
##################################################################

def MergeSort(array):
    if type(array) != list:
        return
    #TODO: Also, check to see that the items in the list are all integers/float

    #Base case: A list of zero or 1 elements is sorted.
    if len(array) <= 1:
        return array

    #Recursive case. DIVIDE the list into equal sized sublists.
    median = len(array)/2
    median = int(median)
    leftArray = []
    rightArray = []
    
    for i in range(0, median):
        leftArray.append(array[i])

    for i in range(median, len(array)):
        rightArray.append(array[i])

    #Recursively sorting both sublists by calling this function again.
    leftArray = MergeSort(leftArray)
    rightArray = MergeSort(rightArray)

    #CONQUER by merging the now sorted left and right sublists
    return Merge(leftArray, rightArray)

def Merge(leftArray, rightArray):
    result = []

    while(len(leftArray) > 0 or len(rightArray) > 0):
        if (len(leftArray) > 0 and len(rightArray) > 0):
            #compare the smallest element of both sublists and put smaller in result
            if leftArray[0] <= rightArray[0]:
                result.append(leftArray[0])
                leftArray.pop(0)
            else:
                result.append(rightArray[0])
                rightArray.pop(0)
        elif len(leftArray) > 0:
            #only this array has elements left to put in "result" list
            result.append(leftArray[0])
            leftArray.pop(0)
        elif len(rightArray) > 0:
            result.append(rightArray[0])
            rightArray.pop(0)

    return result
