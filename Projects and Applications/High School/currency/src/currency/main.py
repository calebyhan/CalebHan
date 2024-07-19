import currency.functions as functions
import requests

def convert(input_currency, output_currency, amount=1, roundTo=2):
    if not functions.check(input_currency.upper()):
        raise ValueError("Invalid input currency: " + input_currency)
    if not functions.check(output_currency.upper()):
        raise ValueError("Invalid output currency: " + output_currency)
    if amount <= 0:
        raise ValueError("Input amount must be positive.")
    url = "http://floatrates.com/daily/" + input_currency + ".json"
    data = requests.get(url).json()[output_currency.lower()]
    return format(round(amount * data["rate"], roundTo), '.' + str(roundTo) + 'f')


def rate(input_currency, output_currency, roundTo=2):
    if not functions.check(input_currency.upper()):
        raise ValueError("Invalid input currency " + input_currency)
    if not functions.check(output_currency.upper()):
        raise ValueError("Invalid output currency " + output_currency)
    url = "http://floatrates.com/daily/" + input_currency + ".json"
    data = requests.get(url).json()[output_currency.lower()]
    return format(round(data["rate"], roundTo), '.' + str(roundTo) + 'f')


def add(values, output_currency, roundTo=2):
    for value in values:
        if not functions.check(value[1].upper()):
            raise ValueError("Invalid input currency: " + value[1])
        if value[0] <= 0:
            raise ValueError("Input amount must be positive.")
    if not functions.check(output_currency.upper()):
        raise ValueError("Invalid output currency: " + value[1])
    output = 0
    for value in values:
        url = "http://floatrates.com/daily/" + value[1] + ".json"
        data = requests.get(url).json()[output_currency.lower()]
        output += value[0] * data["rate"]
    return format(round(output, roundTo), '.' + str(roundTo) + 'f')