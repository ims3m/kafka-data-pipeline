from kafka import KafkaConsumer
import json
import logging

logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "food-orders-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

for msg in consumer:
    event = msg.value

    if event["event_type"] == "order_created":
        logger.info(event)

    elif event["event_type"] == "order_cancelled":
        logger.info(event)
