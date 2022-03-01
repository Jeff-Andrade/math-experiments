import numpy as np


class decimal_binary:

    def __init__(self, number):

        self.binaryList = []
        self.bitValues = []
        self.number = number
        self.power = 0

    def nearest_power(self, number):

        powerResult = 0

        while 2**powerResult <= number:

            powerResult += 1

        self.power = powerResult

    def create_lists(self):

        def add_zeroes(args):

            for i in range(args):

                self.binaryList.append(0)

        def add_values(args):

            for i in range(args):

                self.bitValues.append(2**i)

        add_zeroes(self.power)
        add_values(self.power)

    def conversion(self):

        currentValue = 0

        while currentValue < self.number - 1:

            currentValue = np.dot(self.binaryList, self.bitValues)

            for i in range(len(self.binaryList)):

                if self.binaryList[i] == 0:

                    self.binaryList[i] += 1

                    for j in range(i):

                        self.binaryList[j] = 0

                    break

    def show_result(self):

        self.binaryList.reverse()
        self.binaryList = [str(x) for x in self.binaryList]
        self.binaryList = "".join(self.binaryList)

        print(self.binaryList)

    def activate(self):

        self.nearest_power(self.number)
        self.create_lists()
        self.conversion()
        self.show_result()
    