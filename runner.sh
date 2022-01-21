#!/usr/bin/env bash
# Setup Environment
sh startup.sh

# Run ZooKeeper using properties in config directory
/usr/bin/zookeeper-server-start config/zookeeper.properties

# Run Kafka server  using properties in config directory
/usr/bin/kafka-server-start config/server.properties

#Create Kafka topic manually
/usr/bin/kafka-topics --create  --partitions 1 --replication-factor 1 --topic <topic name>  --bootstrap-server localhost:<port>
/usr/bin/kafka-topics --create  --partitions 1 --replication-factor 1 --topic crimes.calls  --bootstrap-server localhost:9092

# Check list of existing Kafka topics
/usr/bin/kafka-topics --zookeeper localhost:2181 --list

# Consume messages from a topic --optional parameter: --max-message 10
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic crimes.calls --from-beginning --max-message 10

#Run transformation and analytics on consumed messages
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

# Check topic info
/usr/bin/kafka-topics --zookeeper localhost:2181 --topic crimes.calls --describe