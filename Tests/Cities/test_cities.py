import unittest
from city_function import get_formatted_city_name

class TestCityCountry(unittest.TestCase):

    def test_city_country(self):
        formatted_city_name = get_formatted_city_name('rostov','russia')
        self.assertEqual(formatted_city_name,'Rostov,Russia')
    def test_city_country_population(self):
        formatted_city_name = get_formatted_city_name('rostov','russia',1000000)
        self.assertEqual(formatted_city_name,'Rostov,Russia - Population 1000000')

if __name__ == '__main__':
    unittest.main()