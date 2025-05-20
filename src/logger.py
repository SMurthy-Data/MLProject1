import logging,os
from datetime import datetime

LOG_FILE=f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'
LOG_DIR=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_DIR,exist_ok=True)

LOG_PATH= os.path.join(LOG_DIR,LOG_FILE)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

