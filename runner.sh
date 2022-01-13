#!/usr/bin/env bash
# Setup Environment
sh /startup.sh


# ZooKeeper operations
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties


/usr/bin/zookeeper-server-start zookeeper.properties
/usr/bin/kafka-server-start producer.properties


# Runner
/usr/bin/zookeeper-server-start config/zookeeper.properties
/usr/bin/kafka-server-start config/server.properties

touch consumer_server.py

# On Workspace
bin/kafka-console-consumer.sh --bootstrap-server localhost:<your-port-number> --topic <your-topic-name> --from-beginning

# Consume
/usr/bin/kafka-consumer-console --bootstrap-server localhost:9092 --topic daily-incidents --from-beginning





# Test Kafka servver
bin/kafka-console-consumer.sh --bootstrap-server localhost:<your-port-number> --topic <your-topic-name> --from-beginning


spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

