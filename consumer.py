import pika, time


def callback(ch, method, properties, body):
    name = body.decode()
    print(f" [x] Received {name}")
    time.sleep(5)  # simulate processing time
    print(f" [x] Done processing {name}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume_names():
    """
    Consume names from the RabbitMQ queue.
    """
    queue_name = "name_queue"
    credentials = pika.PlainCredentials("admin", "admin@123")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", 5673, "/", credentials)
    )
    channel = connection.channel()

    # Declare the queue (idempotent operation)
    channel.queue_declare(queue=queue_name, durable=True)

    # Set prefetch count to 1 to handle one message at a time
    channel.basic_qos(prefetch_count=1)

    # Subscribe to the queue
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(f" [*] Waiting for message. To exist press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    consume_names()
