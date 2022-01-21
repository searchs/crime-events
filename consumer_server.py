import confluent_kafka
from confluent_kafka import Consumer, OFFSET_BEGINNING
import time
import json


KAFKA_TOPIC = "crimes.calls"
BOOTSTRAP_SERVER = "localhost:9092"
GROUP_ID = "consume_calls"


def run_topic_consumer():

    broker_properties = {
        "bootstrap.servers": BOOTSTRAP_SERVER,
        "group.id": GROUP_ID,
        "default.topic.config": {"auto.offset.reset": "earliest"},
    }

    #     Kafka Consumer
    consumer = Consumer(broker_properties)

    #     Subscribe  to topic
    consumer.subscribe([KAFKA_TOPIC])

    #     Poll messages
    while True:
        print("Chopping topic messages")
        result_count = 1
        while result_count > 0:
            message = consumer.poll(1)
            if message is None:
                result_count = 0
                print("Message don pafuka!")
            elif message.error() is not None:
                result_count = 0
                print("Error dey o")
            else:
                json_data = json.loads(message.value().decode("utf-8"))
                print(json_data)
                result_count = 1
            time.sleep(1)
    consumer.close()


if __name__ == "__main__":
    run_topic_consumer()
