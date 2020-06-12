# Standard library imports
import locale

locale.setlocale(locale.LC_ALL, '') # move to main
currency_symbol = locale.localeconv()["currency_symbol"]
thousands_separator = locale.localeconv()['mon_thousands_sep']

def currency_formatter(value):
    return locale.currency(value)

def strip_currency_formatting(value):
    return value.replace(currency_symbol, "").replace(thousands_separator, "")

def append_currency_symbol(value):
    return f'{value}, {currency_symbol}'

def number_formatter(value):
    return strip_currency_formatting(currency_formatter(value))
