import pika
import time

def callback(ch, method, properties, body):
    print(f" [v] Received event: {body.decode()}")
    
    time.sleep(2) 
    
    print(" [x] Event processing complete.\n")

def start_consuming():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='task_queue')

    channel.basic_consume(
        queue='task_queue',
        on_message_callback=callback,
        auto_ack=True # Automatically acknowledges the message as soon as it's received
    )

    print(' [*] Waiting for events. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consuming()
