import pika
import time

def send_events():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

    print("Starting event producer...")
    
    for i in range(1, 6):
        message = f"Event {i}: Processing microservice data for suilens..."
        
        channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message
        )
        print(f" [x] Sent: '{message}'")
        time.sleep(1)

    connection.close()

if __name__ == '__main__':
    send_events()
