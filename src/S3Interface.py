import os
import logging
from time import gmtime, strftime

currentTime = strftime("%Y-%m-%d:%H:%M:%S", gmtime())
logFile = f'/tmp/bioda/logs/s3InterfaceLogs{currentTime}.log'
dbFile = '/home/zaz/bioda/database'
s3Bucket = 's3://andrew-zhang-backup-bucket'

logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w', format='%(asctime)s %(message)s')

try:
    sync_command = f"aws s3 sync {dbFile} {s3Bucket}"
    logging.info(f"Starting S3 sync/upload from {dbFile} to {s3Bucket}...")
    os.system(sync_command)
    returnCode = os.system("echo $?")
    logging.info(f"The return code for S3 sync is {returnCode}")
    if not returnCode == 0:
        raise FileNotFoundError
except FileNotFoundError as e:
    logging.error("Exception has occurred", exc_info=True)
else:
    logging.info("Sync has completed successfully")
finally:
    logging.info("End of sync")


#TODO: tasks:
#know how to blast from cli write to file

#put program into functions
#simple queue service- start with rabbitmq for local msgqueue