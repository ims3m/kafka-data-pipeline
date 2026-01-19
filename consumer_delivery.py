import json
import logging
from kafka import KafkaConsumer

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
)

logger = logging.getLogger(__name__)

consumer = KafkaConsumer(
    "delivery-status-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="delivery-consumer-v1",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
)

try:
    for msg in consumer:
        logger.info(
            "Recieved message: topic=%s partition=%s offset=%s payload=%s",
            msg.topic,
            msg.partition,
            msg.offset,
            msg.value,
        )
except Exception as e:
    logger.error(f"An exception occurred: {e}")
finally:
    consumer.close()
