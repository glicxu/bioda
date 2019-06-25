# Blast Workflow Design
In this document, we describe the workflow for blast search. The workflow contains the following steps:
1. User submitted a query request, with query file, search_type, and query db
2. Upon user submscribe the workflow for blast search. The workflow contains the following steps:
1. User submitted a query request, with query file, search_type, and query db
2. Upon user submission, bioda persist those request into a database, and return user with a work reference_id, which user can use to get result
3. Job creation: JobManager create new from database with following step:
  a. read from database for all new search jobs
  b. For each job, create a json message and send the message to BlastSearch MessageQ
4.BlastWoker: BlastWorker subscribes to BlastSearch MQ, procese the received message, and return the result into BlastResult MQ

## Steps for JobManager to ission, bioda persist those request into a database, and return user with a work reference_id, which user can use to get result
3. Job creation: JobManager create new from database with following step:
  a. read from database for all new search jobs
  b. For each job, create a json message and send the message to BlastSearch MessageQ
4.BlastWoker: BlastWorker subscribes to BlastSearch MQ, procese the received message, and return the result into BlastResult MQ

## Steps for JobManager to create a new job
1. Creat an empty Python Dictionary 
2. Fill in the value for the following name: job_id, query_filename, search_db, query_type (start with hard value)
3. convert python dict into json using json.dumps
4. send json message into BlastSearch Queue

## Steps for BlastWorker to process a job
1. A worker is starte and run continously listening to BlastSearch queue
2. Upon receiving a new message, proces the message
3. Processing:
  a. convert json message into a Python dictionary
  b. using the values from the converted dictionary as search paramenter to call BlastSearch function
  c. Create ResultMessage with the following data item: job_id, finish_status, output filename
  d. publish ResultMessage into BlastResult Queue
  
## ResultProcessor 
  



