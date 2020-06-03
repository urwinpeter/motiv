import locale
import logging.config
import json
from motivate.controllers.controller import PageController
 

def main():
    with open('logconfig.json') as fh:
        logging.config.dictConfig(json.load(fh))
    log = logging.getLogger(__name__)
    log.info('PROGRAMME START')

    PageController().start_app()

if __name__ == "__main__":
    main()
