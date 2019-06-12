import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='blastresultq')

channel.basic_publish(exchange='', routing_key='blastresultq', body='Hello World!')
print(" [x] Sent 'Hello World!'")

connection.close()