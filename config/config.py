from time import gmtime, strftime


# general variables
currentTime = strftime("%Y-%m-%d:%H:%M:%S", gmtime())


# S3Interface variables
logFile = '/home/zaz/bioda/logs/s3InterfaceLog.log'
dbFile = '/home/zaz/bioda/database'
s3Bucket = 's3://andrew-zhang-backup-bucket'


# Datadownload variables
websiteList = [{'siteHome': "ftp.ncbi.nlm.nih.gov", 'siteSubDir': "blast/db", 'logFile': "/tmp/bioda/logs/dataDownloadLogs", 'dbFile': "/home/zaz/biodadb/", 'regexEnding': ".gz"},
               {},
               {},
               {}]