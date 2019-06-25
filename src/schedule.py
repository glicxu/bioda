# Schedules dataDownload, S3interface jobs
from crontab import CronTab

cron = CronTab(user='zaz')

# dataDownloadJob every 2 days
dataDownloadJob = cron.new(command='python3 /home/zaz/bioda/src/datamanagement/Datadownload.py')

# S3Interface job every 2 days
S3InterfaceJob = cron.new(command='python3 /home/zaz/bioda/src/datamanagement/S3Interface.py')

#if crontab running:
#    cron.remove_all()
#dataDownloadJob.day.every(2)
#cron.write()
#S3InterfaceJob.day.every(2)
#cron.write()


cron.remove_all()
os.system("crontab -r")

# TODO: find way to check for crontab running