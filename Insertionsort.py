########################################################################
#   Neha Gupta
#   Insertionsort Algorithm Implementation
#   Google Jump
#   Under direction of Laura Beth Lincoln
########################################################################

def insert(element, newArray):
    if len(newArray) == 0:
        newArray.append(element)
        return newArray

    for i in range(len(newArray)):
        if element < newArray[i]:
            newArray.insert(i,element)
            return newArray

    newArray.append(element)
    return newArray

def Insertionsort(array):
    if type(array) != list:
        return
    #TODO: check that elements of array are int/float

    newArray = []
    
    while(len(array) != 0):
        element = array.pop()
        newArray = insert(element, newArray)

    return newArray
