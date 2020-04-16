from kombu import Connection, Exchange, Producer, Queue

# instantiate that class and pass it the url of the RabbitMQ server:
rabbit_url = "amqp://localhost:5672/"
conn = Connection(rabbit_url)

# create a channel used when sending messages:
channel = conn.channel()

# specify the exchange
exchange = Exchange("Example-exchange-test1", type="direct")

# create a producer
producer = Producer(exchange=exchange, channel=channel, routing_key="BOB")

# create a queue to send a messase to
queue = Queue(name="Example-queue-test1", exchange=exchange, routing_key="BOB")

# bind the queue to the exchange and then declare it (this actual creates the queue)
queue.maybe_bind(conn)
queue.declare()

# send a message using the producer
producer.publish("Hello World")