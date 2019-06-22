from time import gmtime, strftime


# general variables
currentTime = strftime("%Y-%m-%d__%H:%M:%S", gmtime())


# S3Interface variables
logFile = '/home/zaz/bioda/logs/s3InterfaceLog.log'
dbFile = '/home/zaz/bioda/database'
s3Bucket = 's3://andrew-zhang-backup-bucket'


# Datadownload variables
websiteList = [{'siteHome': "ftp.ncbi.nlm.nih.gov", 'siteSubDir': "blast/db", 'logFile': "/tmp/bioda/logs/dataDownloadLogs", 'dbFile': "/home/zaz/biodadb/ncbi", 'regexEnding': ".gz"},
               {website2},
               {website3},
               {website4}]
dataDownloadLog = '/tmp/bioda/logs'

# TODO: put all log files from config into /tmp/bioda/logs/etc.
# TODO: check out terraform; may use in the future
# Note: "common" subdir used for common fxns used across multiple files