class Riemann:

    def __init__(self, function, bounds, rectangle_amount):

        self.function = function
        self.bounds = bounds
        self.rectangleAmount = rectangle_amount
        self.rectangleLength = (bounds[0] - bounds[1])/self.rectangleAmount

    def summation(self):

        currentValue = 0
        x = 0

        for i in range(self.rectangleAmount):

            x += self.rectangleLength

            y = eval(self.function)

            currentValue += self.rectangleLength * y

        return currentValue
