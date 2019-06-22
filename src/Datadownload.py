from ftplib import FTP
import wget
import os
import logging
from config import config as conf


# downloads from website to /home/zaz/biodadbb
def download(siteHome, siteSubDir, logFile, dbFile, regexEnding):
    logSetup(siteHome, siteSubDir, logFile, dbFile, regexEnding)
    ftpObject = ftpConnect(siteHome, siteSubDir, dbFile, regexEnding)
    ftpDownload(siteHome, siteSubDir, logFile, dbFile, regexEnding, ftpObject)


# checks if dir to write logs to exists; if not, creates one. Then, sets log settings
def logSetup(siteHome, siteSubDir, logFile, dbFile, regexEnding):
    if not os.path.isdir(conf.dataDownloadLog):
        os.makedirs(conf.dataDownloadLog)
    logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='a', format='%(asctime)s %(message)s')


# connects/logins to ftp server, then  cwd to correct subdirectory, then downloads appropriate files
def ftpConnect(siteHome, siteSubDir, dbFile, regexEnding):
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


def ftpDownload(siteHome, siteSubDir, logFile, dbFile, regexEnding, ftp):
    # download
    fileNames = ftp.nlst()
    for file in fileNames:
        logging.info(f"Now downloading {file}...")
        if file.endswith(f"{regexEnding}"):
            localFilePath = os.path.join(f'{dbFile}', file)
            url = f"ftp://{siteHome}/{siteSubDir}/" + file
            wget.download(url, localFilePath)
        logging.info(f"Successfully downloaded {file}.")
    ftp.quit()


def main():
    for item in conf.websiteList:
        download(item['siteHome'], item['siteSubDir'], f"{item['logFile']}{conf.currentTime}.log", item['dbFile'], item['regexEnding'])


if __name__ == "__main__":
    main()

    # TODO: cut down unnecessary parameters from ftpconnect, ftpdownload, logsetup