from crontab import CronTab

cron = CronTab(user='zaz')
job = cron.new(command='/home/zaz/bioda/src/Datadownload.py')
job.hour.every(1)