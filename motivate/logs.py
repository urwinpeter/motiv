import logging
from motivate.item import Item

def log_callbacks(callname):
    def owrapper(func):
        def iwrapper(self, *args, **kwargs):
            log = logging.getLogger(callname)
            log.info(func.__name__)
            func(self, *args, **kwargs)
        return iwrapper
    return owrapper

def log_item(callname):
    def owrapper(class_):
        def iwrapper(*args, **kwargs):
            log = logging.getLogger(callname)
            log.info([arg for arg in args])
            return class_(*args, **kwargs)
        return iwrapper
    return owrapper

def log_db(modulename):
    def owrapper(func):
        def iwrapper(self, item):
            log = logging.getLogger(modulename)
            log.debug(func.__name__)
            log.debug(item.__dict__)
            try:
                func(self, item)    
            except: 
                log.debug('DB Failure')
            log.debug('DB Success')
        return iwrapper
    return owrapper

def log_details(callname):
    def owrapper(func):
        def iwrapper(self, *args, **kwargs):
            log = logging.getLogger(callname)
            details = [e.get() for e in self.entries]
            try:
                item = Item(*details)
                details.append('success')
                log.info(details) 
                return item 
            except ValueError as e:
                details.append('failure')
                mb.showerror("Validation error", str(e), parent=self)
                log.info(details)
        return iwrapper
    return owrapper

        