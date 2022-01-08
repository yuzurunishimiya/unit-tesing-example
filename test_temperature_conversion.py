import unittest

import temperature_conversion as temp_conv


class CelciusToFahrenheitConversionTest(unittest.TestCase):
    def test_input_int(self):
        data: int = 50
        result: float = temp_conv.celcius_to_fahrenheit(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 122.0)

    def test_input_float(self):
        data: float = 50.0
        result: float = temp_conv.celcius_to_fahrenheit(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 122.0)

    def test_input_str(self):
        data: float = "50"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.celcius_to_fahrenheit(data)

    def test_input_seq(self):
        data: list = [50]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.celcius_to_fahrenheit(data)


class CelciusToKelvinConversionTest(unittest.TestCase):
    ...

class FahrenheitToCelciusConversionTest(unittest.TestCase):
    ...

class FahrenheitToKelvinConversionTest(unittest.TestCase):
    ...

class KelvinToCelciusConversionTest(unittest.TestCase):
    ...

class KelvinToFahrenheitConversionTest(unittest.TestCase):
    ...


if __name__ == '__main__':
    unittest.main()
