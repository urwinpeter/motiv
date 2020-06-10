# Standard library imports
import json
import locale
import logging.config

# Local application imports
from motivate.controllers.item_control import  ItemController
from motivate.controllers.money_control import  MoneyController
from motivate.service.money import MoneyService
from motivate.service.items import ItemService
from motivate.views.app import ViewLifecycle


def main():
    with open('logconfig.json') as log_config:
        logging.config.dictConfig(json.load(log_config))
    log = logging.getLogger(__name__)
    log.info('PROGRAMME START')
    
    item_controller=ItemController(ItemService())
    money_controller=MoneyController(MoneyService())
    ViewLifecycle(
                item_controller, money_controller
                ).start_app()

if __name__ == "__main__":
    main()
