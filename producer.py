import pika


def read_names(file_path):
    """
    Read names from a file and return them as a list.
    """
    with open(file_path, "r") as file:
        names = [line.strip() for line in file if line.strip()]
    return names


def send_names_to_queues(names):
    """
    Send each name to the RabbitMQ queue.
    """
    queue_name = "name_queue"
    credentials = pika.PlainCredentials("admin", "admin@123")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost", 5673, "/", credentials)
    )

    channel = connection.channel()

    # Declare the queue (idempotent operation)
    channel.queue_declare(queue=queue_name, durable=True)

    for name in names:
        channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=name,
            properties=pika.BasicProperties(delivery_mode=2),  # Make message persistent
        )

        print(f" [x] send {name}")

    connection.close()


if __name__ == "__main__":
    file_path = "people.txt"
    names = read_names(file_path)
    if names:
        send_names_to_queues(names)
    else:
        print("The file is empty or all lines are blank")
