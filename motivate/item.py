import re
import logging
from motivate.logs import log_item

log = logging.getLogger(__name__)

def required(value, message):
    if not value:
        raise ValueError(message)
    return value

def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)   
    return value

@log_item(log, 'User Item Request:')
class Item():
    category_regex = re.compile(r"^[a-zA-Z]")
    name_regex = re.compile(r"[^@]")
    price_regex = re.compile(r"[0-9]")

    def __init__(self, category='', name='', price=''):
        self.category = category 
        self.name = name
        self.price = price
   
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = matches(value, self.category_regex, "Invalid Category Format")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = matches(value, self.name_regex, "Invalid Name Format")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = matches(value, self.price_regex, "Invalid price format")

@log_item(log, 'DB Item:')
class DBItem():
    def __init__(self, rowid = '', category='', name='', price=''):
        self.rowid = rowid
        self.category = category
        self.name = name
        self.price = price