#   Recall that Python has a built-in function called filter that takes two inputs:
#   The first input is a function f that takes as input a single input and returns either True or False.
#   Such a function is called a predicate. The second input is a list L.
#   The filter function returns a new list that contains all of the elements of L for which the predicate returns True
#   (in the same order as in the original list L).

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def myFilter(predicate, list):

    newList = []
    length = 0
    for n in list:
        length += 1

    for i in range(length):

        if predicate(list[i]):

            newList.append(list[i])

    return newList

#Takes a list of letters and returns True if consonant, False if not
def consonants(X):
    vowels = ['a','e','i','o','u','y']
    count = 0
    for n in vowels:
        count += 1

    for i in range(count):
        if X == vowels[i]:
            return False

    return True

print myFilter(consonants,alphabet)

