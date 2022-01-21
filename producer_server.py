from kafka import KafkaProducer
import json
import time
import datetime
import logging

from confluent_kafka.admin import AdminClient, NewTopic

logger = logging.getLogger(__name__)


class ProducerServer(KafkaProducer):
    def __init__(self, input_file, topic, **kwargs):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.topic = topic

    def read_data_file(self):
        """Read json data file."""
        with open(self.input_file, "r") as src:
            data = json.load(src)
        return data

    # TODO fill this in to return the json dictionary to binary
    @staticmethod
    def dict_to_binary(json_dict):
        return json.dumps(json_dict).encode("utf-8")

    # TODO we're generating a dummy data
    def generate_data(self):
        """Send messages to Kafka topic"""
        with open(self.input_file, "r") as f:
            calls = json.load(f)
            for call in calls:
                message = self.dict_to_binary(call)
                # TODO send the correct data
                self.send(topic=self.topic, value=message)
                time.sleep(1)
