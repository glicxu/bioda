from ftplib import FTP
import wget
import os.path
import logging

from config import config as conf

siteHome = conf.siteHome
siteSubDir = 'blast/db'
logFile = '/home/zaz/bioda/logs/dataDownloadLog.log'
dbFile = '/home/zaz/bioda/database/'
regexEnding = '.gz'

logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w', format='%(asctime)s %(message)s')


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