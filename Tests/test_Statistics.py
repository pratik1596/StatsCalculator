import unittest
import statistics
from Statistics.Statistics import Statistics
from CSVReader.CSVReader import CSVReader
from Statistics.GetSample import getSample
import Statistics.RandomGenerator as tools

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.statistics = Statistics()

    def test_instantiate_statistics(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_getData(self):
        self.assertEqual(len(self.getData()),20)

    def test_getSample(self):
        data = getSample(self.getData(),10)
        self.assertEqual(len(data),10)

    def testMeanStringFails(self):
        data = ['string1','string2','string3']
        self.assertRaises(Exception,self.statistics.mean,data)

    def test_mean(self):
        data = getSample(self.getData(),10)
        print(self.statistics.mean(data))
        self.assertEqual(self.statistics.mean(data), statistics.mean(data))

    def test_medianOdd(self):
        data = getSample(self.getData(),9)
        print(self.statistics.median(data))
        self.assertEqual(self.statistics.median(data), statistics.median(data))

    def test_medianEven(self):
        data = getSample(self.getData(),10)
        print(self.statistics.median(data))
        self.assertEqual(self.statistics.median(data), statistics.median(data))

    def test_mode(self):
        self.assertEqual(self.statistics.mode(tools.getRandomNumbersInt(1,100,50,10)),
                         statistics.mode(tools.getRandomNumbersInt(1,100,50,10)))

    def test_variance(self):
        data = getSample(self.getData(),10)
        self.assertEqual((self.statistics.variance(data)), (statistics.variance(data)))

    def test_standard_deviation(self):
        data = getSample(self.getData(), 10)
        self.assertEqual((int)(self.statistics.standard_deviation(data)),(int)(statistics.stdev(data)))

    def getData(self):
        test_Data = CSVReader('./Tests/Data/Unit Test Sample.csv').data
        data = []
        for row in test_Data:
            num = data.append((int)(row['Value']))
        return data

    def test_getRandomSeed(self):
        value1 = tools.getRandomIntSeed(1,100,50)
        value2 = tools.getRandomIntSeed(1, 100, 50)
        self.assertEqual(value1, value2)

    def test_getRandomSeedList(self):
        value1 = tools.getRandomNumbersInt(1,100,50,10)
        value2 = tools.getRandomNumbersInt(1,100,50,10)
        self.assertEqual(value1, value2)

def test_results_property(self):
    self.assertEqual(self.calculator.result, 0)

if __name__ == '__main__':
    unittest.main()