from kafka import KafkaConsumer
import logging

logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "input-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda v: v.decode("utf-8"),
)


for msg in consumer:
    logger.info(msg)
