from ftplib import FTP
import wget, os.path


ftp = FTP('ftp.ncbi.nlm.nih.gov')
print("logging in...")
ftp.login()
print("changing to /blast/db directory...")
ftp.cwd('blast/db')
print("accessing files...\n\n")


fileNames = ftp.nlst()
for file in fileNames:
    print(file)
    if file.endswith(".gz"):
        localFilePath = os.path.join('/home/zaz/bioda/database/', file)
        url = "ftp://ftp.ncbi.nlm.nih.gov/blast/db/" + file
        wget.download(url, localFilePath)

ftp.quit()
#url = "ftp://ftp.ncbi.nlm.nih.gov/blast/db/16SMicrobial.tar.gz"
#wget.download(url, '/home/zaz/bioda/database')


#scrape all text, put in ary
#for item in ary
#    if item.endswith(.gz):
#        url = ftp://ftp.ncbi.nlm.nih.gov/blast/db/item
#        wget.download(url, '/home/zaz/bioda/database')