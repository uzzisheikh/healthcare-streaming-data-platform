from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

clinical_events = ['admission', 'discharge', 'lab_result', 'medication']

while True:
    event = {
        'patient_id': random.randint(1000, 9999),
        'event_type': random.choice(clinical_events),
        'timestamp': time.time()
    }
    producer.send('clinical_events', value=event)
    print(f"Sent event: {event}")
    time.sleep(2)
