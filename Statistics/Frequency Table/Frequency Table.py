import pandas as pd
import math


class FrequencyTable:

    def __init__(self, data, include_stats):

        def generate_table_info(data):

            classAmount = round(1 + 3.3 * math.log(len(data), 10))
            classAmplitude = (max(data) - min(data))/classAmount
            minValue = min(data)
            maxValue = max(data)

            return [classAmount, classAmplitude, minValue, maxValue]

        self.data = data
        self.include_stats = include_stats

        self.info = generate_table_info(self.data)
        self.classAmount = self.info[0]
        self.classAmplitude = self.info[1]
        self.minValue = self.info[2]
        self.maxValue = self.info[3]

        self.classLines = []

    def generate_interval(self):

        currentValue = self.minValue

        for intervals in range(self.classAmount):

            self.classLines.append(
                [currentValue, currentValue + self.classAmplitude, 0, 0])
            currentValue += self.classAmplitude

    def generate_frequencies(self):

        for numbers in range(len(self.data)):

            for intervals in range(len(self.classLines)):

                if self.data[numbers] >= self.classLines[intervals][0] and self.data[numbers] < self.classLines[intervals][1]:

                    self.classLines[intervals][2] += 1

                elif self.data[numbers] == self.maxValue and self.data[numbers] == self.classLines[intervals][1]:

                    self.classLines[intervals][2] += 1

        for intervals in range(len(self.classLines)):

            self.classLines[intervals][3] = (
                round(self.classLines[intervals][2]/len(self.data), 3))*100

    def generate_stats(self):

        def calculate_mean():

            mean = round(sum(self.data)/len(self.data), 3)

            return mean

        def calculate_median():

            self.data.sort()

            if len(self.data) % 2 == 0:

                median = (self.data[len(self.data)//2] +
                          self.data[(len(self.data)//2) - 1])/2

            else:

                median = self.data[((len(self.data)-1)//2) + 1]

            return median

        def calculate_stdev():

            summation = 0

            for samples in range(len(self.data)):

                summation += (self.data[samples] - calculate_mean())**2

            result = round(math.sqrt((summation/(len(self.data) - 1))), 3)

            return result

        return [calculate_mean(), calculate_median(), calculate_stdev()]

    def get_output(self):

        def get_table():

            dfFrequency = pd.DataFrame(data=self.classLines)
            dfFrequency[0] = dfFrequency[0].round(3)
            dfFrequency[1] = dfFrequency[1].round(3)
            dfFrequency.columns = ["Lower Bound", "Upper Bound",
                                   "Absolute Frequency", "Relative Frequency (%)"]
            dfFrequency.index = range(1, len(dfFrequency.index) + 1)

            return dfFrequency

        def get_stats_table():

            dfStats = pd.DataFrame(data=self.generate_stats())
            dfStats = dfStats.transpose()
            dfStats[0] = dfStats[0].round(3)
            dfStats[1] = dfStats[1].round(3)
            dfStats[2] = dfStats[2].round(3)
            dfStats.columns = ["Mean", "Median",
                               "Standard Deviation"]
            dfStats.index = [1]

            return dfStats

        if self.include_stats == True:

            return [get_table(), get_stats_table()]

        else:

            return [get_table()]

    def run(self):

        if len(self.classLines) == 0:

            self.generate_interval()
            self.generate_frequencies()

            return self.get_output()

        else:

            return self.get_output()
