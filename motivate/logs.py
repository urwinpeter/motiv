# Standard library imports
import logging

def log_user_actions(logger):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            logger.debug(('User Action:', func.__name__, *args))
            func(self, *args, **kwargs)
        return wrapper
    return decorator


def log_db_changes(logger):
    def decorator(func):
        def wrapper(self, item):
            try:
                func(self, item)
                logger.debug(('DB Success:', func.__name__, item.__dict__))    
            except: 
                logger.warning(('DB Failure:', func.__name__, item.__dict__))
        return wrapper
    return decorator


def log_db_items(logger):
    def decorator(func):
        def wrapper(self):
            try:
                for item in func(self):
                    logger.debug(('DB Success:', func.__name__, item.__dict__))
                    yield item     
            except: 
                logger.warning(('DB Failure:', func.__name__))
        return wrapper
    return decorator


def log_user_item(logger, title):
    def decorator(class_):
        def wrapper(*args, **kwargs):
            try: 
                logger.info((title, *args))
                return class_(*args, **kwargs)
            except ValueError as e:
                logger.warning(("Validation error", str(e), *args))
                raise
        return wrapper
    return decorator
        