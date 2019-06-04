import os

sync_command = "aws s3 sync /home/zaz/bioda/database s3://andrew-zhang-backup-bucket --delete"
os.system(sync_command)

#DOWNLOAD: sync_command = "aws s3 sync s3://andrew-zhang-backup-bucket /home/zaz/bioda/database"
#note-sync doesn't delete files, so we add --delete to properly delete files