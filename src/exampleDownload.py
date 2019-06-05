from ftplib import FTP
import wget
import os.path
import logging

siteHome = 'ftp.ncbi.nlm.nih.gov'
siteSubDir = 'blast/db'
logFile = '/home/zaz/bioda/logs/publicDownloadLog.log'
dbFile = '/home/zaz/bioda/database/'
regexEnding = '.gz'

logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w')


ftp = FTP(f'{siteHome}')

logging.info("Preparing to log in...")
try:
    ftp.login()
except IOError as e:
    logging.error("Error logging in. " + e.errno)
else:
    logging.info("Login successful.")

logging.info(f'changing to {siteSubDir} directory...')
try:
    ftp.cwd(f'{siteSubDir}')
except IOError as e:
    logging.error("Error logging in. " + e.errno)
else:
    logging.info(f"successfully changed to {siteSubDir} directory.")

fileNames = ftp.nlst()
for file in fileNames:
    print(file)
    if file.endswith(f"{regexEnding}"):
        localFilePath = os.path.join(f'{dbFile}', file)
        url = f"ftp://{siteHome}/{siteSubDir}/" + file
        wget.download(url, localFilePath)

ftp.quit()

#logs
#functions instead of hardcoding