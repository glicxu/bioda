#User defines parameters of search (sequenceFile, type of search, database, search criteria etc.);
# Organize this data into dictionary, give jobID (which will be used in resultq to retrieve result)

#Job creation: JobManager create new from database with following step:
#    read from database for all new search jobs
#    For each job, create a json message and send the message to BlastSearch MessageQ

## Steps for JobManager to create a new job
# 1. Creat an empty Python Dictionary
# 2. Fill in the value for the following name: job_id, query_filename, search_db, query_type (start with hard value)
# 3. convert python dict into json using json.dumps
# 4. send json message into BlastSearch Queue

import json
import pika


def createJob(id, queryFile, dbFile, queryType):
    jobAttributes = {"job_id": id, "query_filename": queryFile, "search_database": dbFile, "search_type": queryType}
    jobJsonString = json.dump(jobAttributes)

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    #if(queryType == blast) thhen channel.queue.declare(queue=blastworkerqueue)
    #if (queryType == image) thhen channel.queue.declare(queue=imageworkerqueue)
    #switch statement w/ cases
    channel.queue_declare(queue='blastworkerqueue')
    channel.basic_publish(exchange='', routing_key='blastworkerqueue', body=jobJsonString)

def main():
#add hardcoded tests for blastworker, eg createjob(2, lkj.fasta, db.fasta, blastp)
#create job object/class, pass directly to createjob
if __name__ == "__main__":
    main()

    #TODO: make database file that compiles list of job orders, then passes data to thia file (createJobb fxn)