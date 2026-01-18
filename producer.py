import json
import time
import random
import logging
from faker import Faker
from kafka import KafkaProducer

logger = logging.getLogger(__name__)

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

order_events = ["order_created", "order_cancelled"]
delivery_events = ["preparing", "out_for_delivery", "delivered"]

while True:
    user_id = random.randint(1000, 9000)
    order_id = random.randint(1, 1000)

    if random.choice([True, False]):
        event = {
            "event_type": random.choice(order_events),
            "user_id": user_id,
            "order_id": order_id,
            "restaurant": fake.company(),
            "amount": round(random.uniform(10, 50), 2),
            "timestamp": time.time(),
        }

        producer.send("food-orders-topic", event)
        logger.info(event)

    else:
        event = {
            "event_type": random.choice(delivery_events),
            "order_id": order_id,
            "delivery_partner": fake.name(),
            "current_location": fake.city(),
            "timestamp": time.time(),
        }

        producer.send("delivery-status-topic", event)
        logger.info(event)

    producer.flush()
    time.sleep(2)
