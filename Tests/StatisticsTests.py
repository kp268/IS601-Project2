import unittest
import numpy as np
from Statistics.Statistics import Statistics
from RNG.RandomList import random_ints


class StatisticsTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()
        self.testData = random_ints(range(100), 2, 373)
        self.array = np.array(self.testData)

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean(self):
        mean = self.statistics.mean(self.testData)
        self.assertEqual(mean, round(np.mean(self.array), 9))

    def test_median(self):
        median = self.statistics.median(self.testData)
        self.assertEqual(median, round(np.median(self.array), 9))

    def test_mode(self):
        mode = self.statistics.mode(self.testData)
        self.assertEqual(mode, np.argmax(np.bincount(self.testData)))

    def test_variance(self):
        variance = self.statistics.variance(self.testData)
        self.assertEqual(variance, round(np.var(self.array), 9))

    def test_standarddeviation(self):
        standardDeviation = self.statistics.standardDeviation(self.testData)
        self.assertEqual(standardDeviation, round(np.std(self.array), 5))


if __name__ == '__main__':
    unittest.main()
