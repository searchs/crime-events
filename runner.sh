#!/usr/bin/env bash
# Setup Environment
sh startup.sh


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
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092  --topic sf.crime.calls --from-beginning


#Create topic manually
/bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 3 --partitions 2   --topic sf.crime.calls

#Topics list details
/bin/kafka-topics --zookeeper localhost:2181 --list


$ bin/kafka-console-consumer.sh --topic sf.crime.calls quickstart-events --from-beginning --bootstrap-server localhost:9092

# Consume
#Test pub
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic sf.crime.calls --from-beginning

# Test Kafka server
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sf.crime.calls --from-beginning


spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

