from kafka.producer import KafkaProducer
import json
import time


class ProducerServer(KafkaProducer):
    """Produce Kafka messages to a topic from the JSON file
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
            json_data = json.load(f)
            for line in json_data:
                message = self.dict_to_binary(line)
                # TODO send the correct data - Done
                self.send(topic=self.topic, value=message)
                time.sleep(1)

    # TODO fill this in to return the json dictionary to binary - Done
    @staticmethod
    def dict_to_binary(json_dict):
        return json.dumps(json_dict).encode("utf-8")
