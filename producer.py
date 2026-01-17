from kafka import KafkaProducer
import logging

logger = logging.getLogger(__name__)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092", value_serializer=lambda v: v.encode("utf-8")
)

producer.send("input-topic", "Event Data")
producer.flush()
