from ftplib import FTP
import wget
import os
import logging
from config import config as conf



#downloads from website to /home/zaz/bioda
def download(siteHome, siteSubDir, logFile, dbFile, regexEnding):
    #if /tmp/bioda/logs does not exists, create bioda directory
    if not os.path.isdir('/tmp/bioda/logs'):
        os.makedirs('/tmp/bioda/logs')
    logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='a', format='%(asctime)s %(message)s')

    ftp = FTP(f'{siteHome}')

    logging.info(f"Preparing to log in to {siteHome}...")
    try:
        ftp.login()
    except IOError as e:
        logging.error(f"Error logging in to {siteHome}. " + e.errno)
    else:
        logging.info(f"Successfully logged in to {siteHome}.")

    logging.info(f'changing to {siteSubDir} directory...')
    try:
        ftp.cwd(f'{siteSubDir}')
    except FileNotFoundError as e:
        logging.error(f"File Not Found: {siteHome}/{siteSubDir}. " + e.errno)
    else:
        logging.info(f"Successfully cwd to {siteSubDir} directory.")

    fileNames = ftp.nlst()
    for file in fileNames:
        print(file)
        if file.endswith(f"{regexEnding}"):
            localFilePath = os.path.join(f'{dbFile}', file)
            url = f"ftp://{siteHome}/{siteSubDir}/" + file
            wget.download(url, localFilePath)
    ftp.quit()


def main():

    for item in conf.websiteList:
        download(item['siteHome'], item['siteSubDir'], f"{item['logFile']}{conf.currentTime}.log", item['dbFile'], item['regexEnding'])


if __name__ == "__main__":
    main()

    # Done: make siteSubDir-regexEnding called from config as conf
    # Done: list of dicts in conf; each website downloaded from is a dictionary, with siteHome, SubDir, etc. as keys
    # Done: removed green hardcodes
    # TODO: run batch download every, say, 2 days