import re
#from logs import log_item
import logging

def log(callname):
    def owrapper(func):
        def iwrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except ValueError as e:
                log = logging.getLogger(callname)
                log.info(func.__name__)
                log.info(str(e))
                raise ValueError
        return iwrapper
    return owrapper


def required(value, message):
    if not value:
        raise ValueError(message)
    return value

@log(__name__)
def matches(value, regex, message):
    if value and not regex.match(value):
        raise ValueError(message)   
    return value


#@log_item(__name__)
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

#@log_item(__name__)
class DBItem():
    def __init__(self, category='', name='', price=''):
        self.category = category
        self.name = name
        self.price = price