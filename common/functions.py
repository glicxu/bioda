#This contains commonly used functions across several python files
import os
import logging
from config import config as conf


#if logFile doesn't exist, then create logFile. Afterwards, configure logs to APPEND and alert level to INFO
def logSetup(logFile, subDirName):
    if not os.path.isdir(f"{logFile}/datadownloadlogs"):
        os.makedirs(f"{logFile}/datadownloadlogs")
    logging.basicConfig(level=logging.INFO, filename=f'{logFile}/{subDirName}/{conf.currentTime}.log', filemode='a', format='%(asctime)s %(message)s')