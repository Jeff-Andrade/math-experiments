from math import factorial
from random import choice


# Stores all valid permutations of the given data. Valid permutations are those not present in this list
globalPermutations = []


def sampler(data):

    # Stores the permutation generated by one iteration of the sampler function if it is valid permutation
    localPermutation = []
    # Creates a copy of the input data, which will be altered through the execution of the function
    sampleData = data[:]

    # Makes sure that the function will generate a permutation of the same size of the original input data
    while len(localPermutation) < len(data):

        # Chooses a random element from the copy of the data
        sampledElement = choice(sampleData)
        # When an element is chosen, it will be removed from the copy, ensuring that a new element is always picked
        sampleData.remove(sampledElement)
        # Adds the chosen element to the local permutation list
        localPermutation.append(sampledElement)

        if localPermutation in globalPermutations:

            continue  # If the desired number of elements has been reached but the newly generated permutation has already been previously generated, the process will start over again

    # After a valid permutation has been generated, it is added to the global permutation list
    globalPermutations.append(localPermutation)
    print(localPermutation)


def combinations(data):

    # The sampler function will be executed according to the factorial of the number of possible permutations of a list
    for i in range(factorial(len(data))):

        sampler(data)