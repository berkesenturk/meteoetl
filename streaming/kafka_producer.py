from kafka import KafkaProducer
import json, time, random

def produce_stream(bootstrap_servers='localhost:9092', topic='seviri_stream'):
    producer = KafkaProducer(bootstrap_servers=bootstrap_servers,
                             value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    for i in range(10):
        event = {
            'timestamp': time.time(),
            'channel': 'IR_108',
            'brightness': round(280 + random.random()*10, 2),
            'cloud_ratio': round(random.random(), 3)
        }
        producer.send(topic, event)
        print('Produced:', event)
        time.sleep(1)

if __name__ == '__main__':
    produce_stream()