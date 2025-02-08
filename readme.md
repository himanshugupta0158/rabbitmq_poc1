Prerequisites:

- Ensure RabbitMQ is running on your local system, accessible at http://localhost:15672/.
- Install Python (version 3.x is recommended).
- Install the Pika library, which is the recommended Python client for RabbitMQ. You can install it using pip:

Project Structure:

1. Producer (producer.py): Reads names from people.txt and sends them to a RabbitMQ queue named name_queue.
2. Consumer (consumer.py): Receives names from name_queue and prints them every 5 seconds.


producer.py Explanation:

- The read_names function reads names from people.txt and returns a list of names.
- The send_names_to_queue function establishes a connection to RabbitMQ, declares a queue named name_queue, and sends each name to this queue.
- Messages are marked as persistent to ensure they are not lost even if RabbitMQ restarts.


consumer.py Explanation:

- The callback function is invoked whenever a message (name) is received. It simulates processing by sleeping for 5 seconds before acknowledging the message.
- The consume_names function sets up the connection to RabbitMQ, declares the name_queue, and starts consuming messages.
- The basic_qos method with prefetch_count=1 ensures that the consumer processes one message at a time, waiting until the current message is acknowledged before receiving the next.


Running the Project:

1. Ensure RabbitMQ is running on your local system.

2. Place the people.txt file, producer.py, and consumer.py in the same directory.

3. Open a terminal and run the consumer script:
```
python consumer.py
```
The consumer will start and wait for messages.

4. Open another terminal and run the producer script:
```
python producer.py
```
The producer will read names from people.txt and send them to the queue.

5. The consumer will receive each name and print it, simulating processing by waiting 5 seconds between each name.

Notes:

- Ensure that the people.txt file is not empty and contains valid names.
- You can run multiple consumers to see how RabbitMQ distributes messages among them.
- To stop the consumer, press CTRL+C in the terminal where it's running.
> This setup demonstrates how RabbitMQ can be used to decouple the production and consumption of messages, allowing for scalable and efficient processing in Python applications.