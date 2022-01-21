import logging

import producer_server


BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "crimes.calls"
CLIENT_ID = f"producer.{KAFKA_TOPIC}"

logger = logging.getLogger(__name__)


def run_kafka_server():
    # TODO get the json file path - Done
    input_file = "police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=KAFKA_TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVER,
        client_id=CLIENT_ID,
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()
