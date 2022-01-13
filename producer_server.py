from kafka import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):
    """Producve Kafka messages to a topic from the JSON file
        :param input_file:  JSON file for source of events(calls)
        :param topic: Kafka topic to write events to
    """
    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    # TODO we're generating a dummy data - Done
    def generate_data(self):
        with open(self.input_file) as f:
            for line in f:
                message = self.dict_to_binary(line)
                # TODO send the correct data
                self.send(topic=self.topic, value=message)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary - Done
    def dict_to_binary(self, json_dict):
        return json.dumps(json_dict).encode("utf-8")
