import locale
import json
import logging.config
import tkinter as tk
from motivate.controllers.controller import PageController

def main():
    with open('logconfig.json') as log_config:
        logging.config.dictConfig(json.load(log_config))
    log = logging.getLogger(__name__)
    log.info('PROGRAMME START')

    root = tk.Tk()
    PageController(root).start_app()


if __name__ == "__main__":
    main()
