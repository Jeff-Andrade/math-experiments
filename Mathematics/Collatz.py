import matplotlib.pyplot as plt


def collatz(num):

    numList = []

    while num != 1:

        if num % 2 == 0:

            num = num//2
            numList.append(num)

        else:

            num = (3 * num) + 1
            numList.append(num)

        print(num)

    plt.plot(numList)
    plt.show()
