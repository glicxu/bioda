import os

sync_command = "aws s3 sync /home/zaz/bioda/database s3://andrew-zhang-backup-bucket --delete"
#DOWNLOAD: sync_command = "aws s3 sync s3://andrew-zhang-backup-bucket /home/zaz/bioda/database"
#--sync doesn't delete files, so we add --delete to properly delete files
os.system(sync_command)