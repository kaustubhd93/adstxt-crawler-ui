# Rabbitmq

- It is a distributed asynchronous message queue.
- Can be stand alone or a cluster.
- Doesn't retain messages once consumed.
- Runs as a systemd service. Easy to operate.

# Terminologies:

- Producer: Producing means nothing more than sending. A program that sends messages is a producer.
- Queue: A queue is the name for a post box which lives inside RabbitMQ. Although messages flow through RabbitMQ and your applications, they can only be stored inside a queue. A queue is only bound by the host's memory & disk limits, it's essentially a large message buffer. Many producers can send messages that go to one queue, and many consumers can try to receive data from one queue. They exist inside the broker.
- Consumer: Consuming has a similar meaning to receiving. A consumer is a program that mostly waits to receive messages.

# Message flow in RabbitMQ:

- The producer publishes a message to an exchange. When creating an exchange, the type must be specified. This topic will be covered later on.
- The exchange receives the message and is now responsible for routing the message. The exchange takes different message attributes into account, such as the routing key, depending on the exchange type.
- Bindings must be created from the exchange to queues. In this case, there are two bindings to two different queues from the exchange. The exchange routes the message into the queues depending on message attributes.
- The messages stay in the queue until they are handled by a consumer
- The consumer handles the message.

## Exchange inside RabbitMQ.

- The core idea in the messaging model in RabbitMQ is that the producer never sends any message directly to a queue.
- Instead, the producer can only send messages to an exchange. An exchange is a very simple thing. On one side it receives messages from producers and the other side it pushes them to queues. The exchange must know exactly what to do with a message it receives. Should it be appended to a particular queue? Should it be appended to many queues? Or should it get discarded. The rules for that are defined by the exchange type.
- There are a few exchange types available: direct, topic, headers, fanout.
- The exchange parameter is the name of the exchange. The empty string denotes the default or nameless exchange: messages are routed to the queue with the name specified by routing_key, if it exists.
- "exchange" 
