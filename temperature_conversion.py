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
    return (celcius * 9/5) + 32

@numeric_accepted
def celcius_to_kelvin(celcius: TEMP) -> float:
    return celcius + 273.15

@numeric_accepted
def fahrenheit_to_celcius(fahrenheit: TEMP) -> float:
    return (fahrenheit - 32) * 5/9

@numeric_accepted
def fahrenheit_to_kelvin(fahrenheit: TEMP) -> float:
    return (fahrenheit - 32) * 5/9 + 273.15

@numeric_accepted
def kelvin_to_celcius(kelvin: TEMP) -> float:
    return kelvin - 273.15

@numeric_accepted
def kelvin_to_fahrenheit(kelvin: TEMP) -> float:
    return (kelvin - 273.15) * 9/5 + 32
