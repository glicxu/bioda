#job manager to blastsearchq to batchblast to result q to results processor
#BlastWorker subscribes to BlastSearch MQ, processes the received message, and return the result into BlastResult MQ

## Steps for BlastWorker to process a job
# 1. A worker is starte and run continously listening to jobCreator.py queue
# 2. Upon receiving a new message, proces the message
# 3. Processing:
#   a. convert json message into a Python dictionary
#   b. using the values from the converted dictionary as search paramenter to call BlastSearch function
#   c. Create ResultMessage with the following data item: job_id, finish_status, output filename
#   d. publish ResultMessage into BlastResult Queue

import pika
import os

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

print("Listing queues: ")
os.system("sudo rabbitmqctl list_queues")


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='blastworkerqueue', auto_ack=True, on_message_callback=callback)
#read from bwqueue
#use blastsearch.py to process job
#send to resultqueue
#TODO: move blastworkerq to conf.bwqueue
#todo: write tests

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()