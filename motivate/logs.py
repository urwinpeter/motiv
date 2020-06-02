import logging

def log_callbacks(logger):
    def owrapper(func):
        def iwrapper(self, *args, **kwargs):
            logger.debug(('User Action:', func.__name__, *args))
            func(self, *args, **kwargs)
        return iwrapper
    return owrapper

def log_db(logger):
    def owrapper(func):
        def iwrapper(self, item):
            try:
                func(self, item)
                logger.debug(('DB Success:', func.__name__, item.__dict__))    
            except: 
                logger.warning(('DB Failure:', func.__name__, item.__dict__))
        return iwrapper
    return owrapper

def log_item(logger, title):
    def owrapper(class_):
        def iwrapper(*args, **kwargs):
            try: 
                logger.info((title, *args))
                return class_(*args, **kwargs)
            except ValueError as e:
                logger.warning(("Validation error", str(e), *args))
                raise
        return iwrapper
    return owrapper

'''def log_details(callname):
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
    return owrapper'''

        