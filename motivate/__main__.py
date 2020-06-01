import locale
from motivate.controllers.controller import PageController
import datetime
import logging
import json
from logging import config

with open('logconfig.json') as fh:
    config.dictConfig(json.load(fh))


#logging.config.fileConfig(fname='logconfig.conf')


log  = logging.getLogger()
log.info(datetime.datetime.now())

log = logging.getLogger(__name__)
log.info('Hello')

def main():

    PageController().start_app()

if __name__ == "__main__":
    main()


'''root = tk.Tk()

home = HomeController(root)
login = LoginController(root, home)'''
