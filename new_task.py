import pika, sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()



# Check for a queue and create it, if necessary
channel.queue_declare(queue='hello')

message = ' '.join(sys.argv[1:]) or "Hello World!"

# For the sake of simplicity, we are not declaring an exchange, so the subsequent publish call will be sent to a Default exchange that is predeclared by the broker
channel.basic_publish(exchange='', routing_key='hello', body=message)
print(" [x] Sent 'Hello World!'")

# Safely disconnect from RabbitMQ
connection.close() 