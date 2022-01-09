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
    def test_input_int(self):
        data: int = 50
        result: float = temp_conv.celcius_to_kelvin(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 323.15)

    def test_input_float(self):
        data: float = 50.0
        result: float = temp_conv.celcius_to_kelvin(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 323.15)

    def test_input_str(self):
        data: float = "50"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.celcius_to_kelvin(data)

    def test_input_seq(self):
        data: list = [50]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.celcius_to_kelvin(data)


class FahrenheitToCelciusConversionTest(unittest.TestCase):
    def test_input_int(self):
        data: int = 100
        result: float = temp_conv.fahrenheit_to_celcius(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 37.78)

    def test_input_float(self):
        data: float = 100.57
        result: float = temp_conv.fahrenheit_to_celcius(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 38.09)

    def test_input_str(self):
        data: float = "100"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.fahrenheit_to_celcius(data)

    def test_input_seq(self):
        data: list = [100]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.fahrenheit_to_celcius(data)


class FahrenheitToKelvinConversionTest(unittest.TestCase):
    def test_input_int(self):
        data: int = 100
        result: float = temp_conv.fahrenheit_to_kelvin(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 310.93)

    def test_input_float(self):
        data: float = 100.69
        result: float = temp_conv.fahrenheit_to_kelvin(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 311.31)

    def test_input_str(self):
        data: float = "100"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.fahrenheit_to_kelvin(data)

    def test_input_seq(self):
        data: list = [100]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.fahrenheit_to_kelvin(data)


class KelvinToCelciusConversionTest(unittest.TestCase):
    def test_input_int(self):
        data: int = 300
        result: float = temp_conv.kelvin_to_celcius(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 26.85)

    def test_input_float(self):
        data: float = 300.69
        result: float = temp_conv.kelvin_to_celcius(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 27.54)

    def test_input_str(self):
        data: float = "300"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.kelvin_to_celcius(data)

    def test_input_seq(self):
        data: list = [300]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.kelvin_to_celcius(data)


class KelvinToFahrenheitConversionTest(unittest.TestCase):
    def test_input_int(self):
        data: int = 300
        result: float = temp_conv.kelvin_to_fahrenheit(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 80.33)

    def test_input_float(self):
        data: float = 300.69
        result: float = temp_conv.kelvin_to_fahrenheit(data)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 81.57)

    def test_input_str(self):
        data: float = "300"
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.kelvin_to_fahrenheit(data)

    def test_input_seq(self):
        data: list = [300]
        with self.assertRaises(TypeError, msg="unsupported operand"):
            temp_conv.kelvin_to_fahrenheit(data)


if __name__ == '__main__':
    unittest.main()
