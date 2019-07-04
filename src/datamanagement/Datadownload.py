from ftplib import FTP #file transfer protocol
import wget #wget downloads from url to localFilepath
import os #system commands
import logging #info logs, error logs, etc.
import re #regex to search and download appropriate files
from config import config as conf


# downloads from website to /home/zaz/biodadbb
def download(siteHome, siteSubDir, logFile, dbFile, regexEnding):
    logSetup(logFile)
    dbSetup(dbFile)
    ftpObject = ftpConnect(siteHome, siteSubDir)
    ftpDownload(siteHome, siteSubDir, dbFile, regexEnding, ftpObject)


def logSetup(logFile):
    if not os.path.isdir(logFile):
        os.makedirs(logFile)
    logging.basicConfig(level=logging.INFO, filename=f'{logFile}/{conf.currentTime}.log', filemode='a', format='%(asctime)s %(message)s')


def dbSetup(dbFile):
    if not os.path.isdir(dbFile):
        os.makedirs(dbFile)


# connects/logins to ftp server, then  cwd to correct subdirectory, then downloads appropriate files
def ftpConnect(siteHome, siteSubDir):
    # connects
    ftp = FTP(f'{siteHome}')
    logging.info(f"Preparing to log in to {siteHome}...")
    try:
        ftp.login()
    except IOError as e:
        logging.error(f"Error logging in to {siteHome}. " + e.errno)
    else:
        logging.info(f"Successfully logged in to {siteHome}.")
    # cwd
    logging.info(f'changing to {siteSubDir} directory...')
    try:
        ftp.cwd(f'{siteSubDir}')
    except FileNotFoundError as e:
        logging.error(f"File Not Found: {siteHome}/{siteSubDir}. " + e.errno)
    else:
        logging.info(f"Successfully cwd to {siteSubDir} directory.")
    return ftp


def ftpDownload(siteHome, siteSubDir, dbFile, regexEnding, ftp):
    # download
    fileNames = ftp.nlst()
    logging.info(f"Now downloading all files with regex '*{regexEnding}'...")
    fileRegex = re.compile(rf'*{regexEnding}')
    for file in fileNames:
        if fileRegex.match(file):
            localFilePath = os.path.join(f'{dbFile}', file)
            url = f"ftp://{siteHome}/{siteSubDir}/" + file
            logging.info(f"Now downloading {file}...")
            wget.download(url, localFilePath)
            logging.info(f"Successfully downloaded {file}.")
    ftp.quit()


def main():
    for item in conf.websiteList:
        download(item['siteHome'], item['siteSubDir'], f"{item['logFile']}", item['dbFile'], item['regexEnding'])


if __name__ == "__main__":
    main()

    #TODO: add in a check to see if /home/zaz/biodadb/ncbi is a dir, then create one if false
    #TODO: don't write logs into /tmp/bioda/logs/ncbi/10am, put into /tmp/bioda/logs/dataDownloadLogs/ncbi/10am, etc.