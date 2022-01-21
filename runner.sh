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
/usr/bin/kafka-topics.sh --create  --partitions 1 --replication-factor 1    --topic sf.crime.calls  --bootstrap-server localhost:9092
$ bin/kafka-topics.sh --create --partitions 1 --replication-factor 1 --topic quickstart-events --bootstrap-server localhost:9092
#Topics list details
/bin/kafka-topics --zookeeper localhost:2181 --list


$ bin/kafka-console-consumer.sh --topic sf.crime.calls quickstart-events --from-beginning --bootstrap-server localhost:9092

# Consume
#Test pub
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic sf.crime.calls --from-beginning

# Test Kafka server
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sf.crime.calls --from-beginning


spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

# ZooKeeper operations
bin/zookeeper-server-start.sh config/zookeeper.properties
bin/kafka-server-start.sh config/server.properties


/usr/bin/zookeeper-server-start zookeeper.properties
/usr/bin/kafka-server-start producer.properties


# Runner
/usr/bin/zookeeper-server-start config/zookeeper.properties
/usr/bin/kafka-server-start config/server.properties

touch consumer_server.py

# Analytics: Run data_stream [update spark.conf with the spark-sql-kafka ]
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py

# Manually create topic
kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 2 --topic crimes.calls

# On Workspace
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sf.crime.calls --from-beginning --max-message 10

# Consume
/usr/bin/kafka-consumer-console --bootstrap-server localhost:9092 --topic crime.calls --from-beginning


# Test Kafka server
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <your-topic-name> --from-beginning

/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic sfrancisco.crime.calls --from-beginning
/usr/bin/kafka-console-consumer --bootstrap-server localhost:9092 --topic sfrancisco.crime.calls --from-beginning  --max-messages 10


spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.4 --master local[*] data_stream.py


# Check topic info
/usr/bin/kafka-topics --zookeeper localhost:2181 --topic sf.crime.calls --describe

# Delete topic
/usr/bin/kafka-topics --zookeeper localhost:2181 --topic sf.crime.calls --delete
