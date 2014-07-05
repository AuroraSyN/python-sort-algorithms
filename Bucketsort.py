###############################################################################
#   Neha Gupta
#   Coded for Google Jump
#   Bucket sort
#   Under direction of Laura Beth Lincoln
#   So it looks to me from searching online that there's a lot of variations
#   to bucket sort? Here, I'm choosing to implement one with a number of buckets
#   specified. It looks like instead, you could be given a max number of values
#   per bucket, or some kind of distribution algorithm/pattern (0-9, 10-20..)
#   This one seems really ineffecient to me :/
###############################################################################
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

def Bucketsort(array, num_buckets):
    '''
    array is the values we're sorting
    num_buckets is the number of buckets given
    '''
    if type(array) != list or type(num_buckets) != int:
        return "Input to sort must be list, and number of buckets must be list"
    if len(array) < 2:
        return array

    buckets = []
    for i in range(num_buckets):
        print(i)
        buckets.append([])
    #buckets will be a list of lists. The number of elements in buckets will
    #be the number of buckets the user specified
    bucketnum = 0
    for i in array:
        buckets[bucketnum].append(i)
        bucketnum += 1
        if bucketnum == num_buckets:
            bucketnum = 0

    print(buckets)
    for i in range(len(buckets)):
        buckets[i] = Insertionsort(buckets[i])

    print(buckets)
    combined_array = []
    for i in range(num_buckets):
        for element in buckets[i]:
            combined_array.append(element)

    combined_array = Insertionsort(combined_array)
    print(combined_array)
