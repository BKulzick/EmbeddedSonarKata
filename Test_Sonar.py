import unittest
from unittest.mock import MagicMock
from Sonar import distanceMeasurement

class TestStringMethods(unittest.TestCase):
  
    @mock.patch('Adafruit_BBIO.output')
    @mock.patch('Adafruit_BBIO.input')
    def test_distanceMeasurement(self):
        ECHO_PIN = "P8_11"
        TRIGGER_PIN = "P8_12"
        distanceMeasurement(TRIGGER_PIN,ECHO_PIN)

        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()