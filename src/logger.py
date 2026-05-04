import os
import logging
from datetime import datetime

LOG_FILE = f'{datetime.now().strftime("%m-%d-%Y_%H-%M-%S")}.log'
LOG_PATH = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

"""
if __name__ == "__main__":
    logging.info("This is an info message.")
    logging.warning("This is a warning message.")
    logging.error("This is an error message.")
"""