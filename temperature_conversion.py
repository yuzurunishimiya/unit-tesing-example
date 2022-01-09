# create an example of code, and then create unit testing
from typing import TypeVar

TEMP = TypeVar("TEMP", float, int)

# still raise TypeError, will be update in the future
def numeric_accepted(func):
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return res
        except TypeError:
            raise TypeError

    return inner

@numeric_accepted
def celcius_to_fahrenheit(celcius: TEMP) -> float:
    return round((celcius * 9/5) + 32, 2)

@numeric_accepted
def celcius_to_kelvin(celcius: TEMP) -> float:
    return round(celcius + 273.15, 2)

@numeric_accepted
def fahrenheit_to_celcius(fahrenheit: TEMP) -> float:
    return round((fahrenheit - 32) * 5/9, 2)

@numeric_accepted
def fahrenheit_to_kelvin(fahrenheit: TEMP) -> float:
    return round((fahrenheit - 32) * 5/9 + 273.15, 2)

@numeric_accepted
def kelvin_to_celcius(kelvin: TEMP) -> float:
    return round(kelvin - 273.15, 2)

@numeric_accepted
def kelvin_to_fahrenheit(kelvin: TEMP) -> float:
    return round((kelvin - 273.15) * 9/5 + 32, 2)
