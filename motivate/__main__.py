import locale
import json
import logging.config
import tkinter as tk
from motivate.controllers.controller import LoginController, HomeController
from motivate.views.pages import ViewLifecycle

def main():
    with open('logconfig.json') as log_config:
        logging.config.dictConfig(json.load(log_config))
    log = logging.getLogger(__name__)
    log.info('PROGRAMME START')
    
    login_controller=LoginController()
    home_controller=HomeController()

    ViewLifecycle(
        login_controller, home_controller
    ).start_app()



if __name__ == "__main__":
    main()
