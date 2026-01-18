#!/bin/bash
set -e

log_info() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') [INFO] $1"
}

log_warn() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') [WARN] $1"
}

log_error() {
  echo "$(date '+%Y-%m-%d %H:%M:%S') [ERROR] $1"
}

docker compose up -d

sleep 10

docker exec kafka kafka-topics \
  --bootstrap-server kafka:9092 \
  --create \
  --if-not-exists \
  --topic food-orders-topic \
  --partitions 1 \
  --replication-factor 1

docker exec kafka kafka-topics \
  --bootstrap-server kafka:9092 \
  --create \
  --if-not-exists \
  --topic delivery-status-topic \
  --partitions 1 \
  --replication-factor 1

python producer.py

sleep 10

python consumer_order.py &
python consumer_delivery.py &

wait
