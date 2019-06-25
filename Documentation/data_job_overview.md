##Data

1. Data is downloaded from source -> local -> s3.

2. Data is organized; incremental update strategy, version, catalogue

##Job

1. User defines parameters of search (sequenceFile, type of search, database, search criteria etc.); given jobID

2. Job sent through queue and classified; sent to appropriate jobWorker

3. Appropriate jobWorker completes task and returns results back to s3.