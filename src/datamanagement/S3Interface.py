import os
import logging
from time import gmtime, strftime
import config from config as conf

currentTime = strftime("%Y-%m-%d:%H:%M:%S", gmtime())
logFile = f'/tmp/bioda/logs/s3InterfaceLogs{currentTime}.log'
dbFile = '/home/zaz/biodadb'

logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w', format='%(asctime)s %(message)s')


# upload sync from local to s3 bucket
def uploadSync(#TODO: add parameters):
    try:
        sync_command = f"aws s3 sync {dbFile} {conf.s3Bucket}"
        logging.info(f"Starting S3 sync/upload from {dbFile} to {conf.s3Bucket/subdirectory}...")
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


def downloadSync(#TODO: add parameters):
    try:
        sync_command = f"aws s3 sync {conf.s3Bucket} {dbFile}"
        logging.info(f"Starting S3 sync/download from {conf.s3Bucket} to {dbFile}...")
        os.system(sync_command)
        returnCode = os.system("echo $?")
        logging.info(f"The return code for S3 sync is {returnCode}")
        if not returnCode == 0:
            raise FileNotFoundError
    except FileNotFoundError #TODO: don't write logs into /tmp/bioda/logs/ncbi/10am, put into /tmp/bioda/logs/dataDownloadLogs/ncbi/10am, etc.as e:
        logging.error("Exception has occurred", exc_info=True)
    else:
        logging.info("Sync has completed successfully")
    finally:
        logging.info("End of sync")


def main():
    for item in conf.websiteList():
        uploadSync(#TODO: add parameters)
        downloadSync(#TODO: add parameters)


if __name__ == "__main__":
    main()

#s3Bucket = 's3://andrew-zhang-backup-bucket'
#dbfile = /home/zaz/biodadb
# TODO: change regex from python ".endswit()" function to a real regex
# TODO: don't write logs into /tmp/bioda/logs/ncbi/10am, put into /tmp/bioda/logs/S3InterfaceLogs/ncbi/10am, etc.
#TODO: for item in conf.websiteLIst loop to sync each website dbfile with it's respective s3bucket subdirectory
#TODO: move all variables to config, remove all hard coded variables INCLUDING log Files
#TODO: simple queue service- start with rabbitmq for local msgqueue
#TODO: know how to blast from cli write to file

#UPLOADSYNC PSEUDOCODE (for each website, e.g. ncbi)
#   sync from /home/zaz/biodadb/ncbi --> s3://andrew_zhang_backup_bucket/ncbi
