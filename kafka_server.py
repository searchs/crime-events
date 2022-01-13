import producer_server

BOOTSTRAP_SERVER = "localhost:9092"
KAFKA_TOPIC = "sf.crime.calls"


def run_kafka_server():
    # TODO get the json file path
    input_file = "data/police-department-calls-for-service.json"

    # TODO fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic=KAFKA_TOPIC,
        bootstrap_servers=BOOTSTRAP_SERVER,
        client_id=f"producer.{KAFKA_TOPIC}",
    )

    return producer


def feed():
    producer = run_kafka_server()
    print("Generating data in a second")
    producer.generate_data()


if __name__ == "__main__":
    feed()
