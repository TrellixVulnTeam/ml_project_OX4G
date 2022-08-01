import logging
from datetime import date, datetime 
import os

LOG_DIR = "logs"
CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
FILE_NAME = f"logs_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR,exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR,FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH
,filemode="w"
,level=logging.INFO
,format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s"
)



