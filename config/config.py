from time import gmtime, strftime


# general variables
currentTime = strftime("%Y-%m-%d__%H:%M:%S", gmtime())


# S3Interface variables
logFile = '/home/zaz/bioda/logs/s3InterfaceLog.log'
dbFile = '/home/zaz/bioda/database'
s3Bucket = 's3://andrew-zhang-backup-bucket'


#temp: list used to store aliases, try to work it into websiteList somehow;
aliasList = ['ncbi', None, None, None]
logDir = '/tmp/bioda/logs' #parent dir to store each website's logs in separate subdirs
dbDir = '/home/zaz/biodadb' #parent dir to store each website's db in separate subdirs
websiteList = [{'siteHome': "ftp.ncbi.nlm.nih.gov", 'siteSubDir': "blast/db", 'logFile': f'{logDir}/{aliasList[0]}', 'dbFile': f'{dbDir}/{aliasList[0]}', 'fileRegexF': ".gz$", 'bucketSubDir': f   "{s3Bucket}/{aliasList[0]}",
               {'''website2'''},
               {'''website3'''},
               {'''website4'''}]

# TODO: change aliasList to a more appropriate way
# TODO: change WebsiteList objects from struct/dictionary to classes/objects
# TODO: have a very systematic way of naming websiteList attributes
# TODO: consistently check github board- work into gcalendar, say, everyday at  9am
# TODO: put all log files from config into /tmp/bioda/logs/etc.
# TODO: check out terraform; may use in the future