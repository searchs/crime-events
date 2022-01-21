from confluent_kafka.admin import AdminClient, NewTopic
import logging


logger = logging.getLogger(__name__)


class KafkaClient:
    def __init(self, bootstrap_servers):
        self.client = AdminClient({"bootstrap.servers": bootstrap_servers})

    def topic_exists(self, topic_name):
        """Checks if provided topic exists"""
        topic_metadata = self.client.list_topics(timeout=5)
        return topic_metadata.topics.get(topic_name) is not None

    def create_topic(self, topic_name, num_partitions, num_replicas):
        """Creates a producer topic"""
        futures = self.client.create_topics(
            [
                NewTopic(
                    topic=topic_name,
                    num_partitions=num_partitions,
                    replication_factor=num_replicas,
                )
            ]
        )

        for k, future in futures.items():
            try:
                future.result()
                logger.info(f"Kafka topic {topic_name} created!")
            except Exception as e:
                logger.info(
                    f"Kafka topic creation failed = {topic_name} with exception: {e} "
                )

# TODO:
# Implement FFT (Fast Fourier transform) algorithm to generate the frequency of SF service calls.
# Try to scale out and figure out the combinations on your local machine number of offsets/partitions. Can you make 2000 offsets per trigger? How can you tell you’re ingesting <offsets> per trigger? What tools can you use?
# Generate dynamic charts/images per batch.