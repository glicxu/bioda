#bioda phase I  project plan

During phase I, we will create a data sync up service to collect public available biological
information, such as dna and protein sequences. We will store these information in S3 and be able
to search against those data with blast program.

1. NCBI data download onto local server

1.1 Manual download

https://www.ncbi.nlm.nih.gov/home/download/

1.2 Download using python 
https://pythonprogramming.net/ftp-transfers-python-ftplib/

1.3 Create download/data sync configuration

1.4 Create a unix cron job to automatically download

2. AWS S3 CLI

2.1 Install AWS CLI
https://docs.aws.amazon.com/cli/latest/userguide/install-linux.html

2.2 modify donwload script to put donwloaded files onto S3 bucket


3. Learn how to use Blast Search
3.1 How blast works
3.2 Download blast program do a local search


4. Search using S3 files

4.1 Set up an EC2 VM
4.2 Run Blast using EC2 VM with S3 data