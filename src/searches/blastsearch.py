import os
import logging

logFile = '/home/zaz/bioda/logs/batchBlastLog.log'
blastResults = "/home/zaz/bioda/blastResults"


#uses ncbi blastp cli to search multiple file
logging.basicConfig(level=logging.INFO, filename=f'{logFile}', filemode='w', format='%(asctime)s %(message)s')
def blastBatchSearch(list, searchtype, database, jobName): #list is list of files to search, searchType is "blastp",etc. dataBase
    #create jobName subdirectory
    #check for exception if folder already exists
    for file in list:
        blastSingleSearch(file, searchtype, database)
    logging.info("End of blast search.")


#blast a single sequence
def blastSingleSearch(file, searchtype, database):
    try:
        outpath = os.path.splitext(f'{blastResults}/{searchtype}/{database}:{file}')[0]
        logging.info(f"Attempting to run {searchtype} on {file} against db {database}...")
        os.system(f'{searchtype} -query {file} -db {database} -out {outpath}.txt')
    except FileNotFoundError as e:
        logging.error("Exception has occurred", exc_info=True)
    except FileExistsError as e:
        logging.error(f"{outpath}.txt already exists. Has been overwritten")
    else:
        logging.info(f"Successfully applied ncbi blast to file: {file}.")

def main():
#todo:if single file, call blastsinglesearch
#todo:else cal blastbatchsearch
#todo: write tests
    #temporary hardcode

if __name__ == "__main__":
    main()

#TODO: test in main to see if both fxns work(main fxns are essentially unit testing)
#TODO: remove hardcoding, reference conf
#TODO: Run Blast using EC2 VM with S3 data
#add jobname
#add exception fileexists or folderexists if file already exists`
#add main- check odin
#rabbitMQ- learn how to enqueue and dequeue
#If time- SQS
#Apache Kafka
#unit testing
#put stuff into main files: blastbatch, S3interface, dataDownload