import os
import logging

logFile = '/home/zaz/bioda/logs/s3UploadLog.log' #/tmp/biodaLog
dbFile = '/home/zaz/bioda/database'
s3Bucket = 's3://andrew-zhang-backup-bucket'

logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w')

try:
    sync_command = f"aws s3 sync {dbFile} {s3Bucket}"
    logging.info("Starting S3 upload from local directory to S3 bucket...")
    os.system(sync_command)
    returnCode = os.system("echo $?")
    if not returnCode == 0:
        raise FileNotFoundError
except FileNotFoundError as e:
    logging.error("Exception has occurred", exc_info=True)
else:
    logging.info("Sync has completed successfully")
finally:
    logging.info("End of sync")


#make timestamp
#note- some variables are duplicates with other files and should be consolidated in a config file