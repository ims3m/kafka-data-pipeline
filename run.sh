#!/bin/bash
set -e

echo "STARTING KAFKA..."
docker compose up -d

sleep 10

echo "CREATING TOPIC..."
docker exec kafka kafka-topics \
  --bootstrap-server localhost:9092 \
  --create \
  --if-not-exists \
  --topic input-topic \
  --partitions 1 \
  --replication-factor 1

echo "STARTING CONSUMER..."
python consumer.py &

sleep 2

echo "STARTING PRODUCER..."
python producer.py
wait