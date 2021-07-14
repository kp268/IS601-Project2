from Calculator.Calculator import Calculator

from Statistics.Mean import findmean
from Statistics.Median import findmedian
from Statistics.Mode import findmode
from Statistics.Variance import findvariance
from Statistics.StandardDeviation import findsd


class Statistics(Calculator):

    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = findmean(data)
        return self.result

    def median(self, data):
        self.result = findmedian(data)
        return self.result

    def mode(self, data):
        self.result = findmode(data)
        return self.result

    def variance(self, data):
        self.result = findvariance(data)
        return self.result

    def standardDeviation(self, data):
        self.result = findsd(data)
        return self.result
