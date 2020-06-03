import re
import logging
from motivate.logs import log_user_item

log = logging.getLogger(__name__)


def matches(value, message, regex):
    if not regex.match(value):
        raise ValueError(message)
    return value


@log_user_item(log, 'User Item Request:')
class Item():
    string_regex = re.compile(r"^\w+( +\w+)*$") # Accept alphanumeric characters with spaces and underscores
    price_regex = re.compile(r"^\d+\.?\d{0,2}$") # Accept number in decimal form

    def __init__(self, category='', name='', price=''):
        self.category = category 
        self.name = name
        self.price = price
   
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = matches(value, "Invalid Category Format", self.string_regex)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = matches(value, "Invalid Name Format", self.string_regex)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = matches(value, "Invalid price format", self.price_regex)


class DBItem():
    def __init__(self, rowid = '', category='', name='', price=''):
        self.rowid = rowid
        self.category = category
        self.name = name
        self.price = price
