import json

from kafka import KafkaProducer

KAFKA_TOPIC = 'events'
KAFKA_BROKERS = '192.168.99.100:9092'

value = '{"id":"0000001","type":"NAV","time":10000,"planeCode":222,"nav_x":1,"nav_y":1,"nav_z":1,"v_x":1,"v_y":1,"v_z":1}'

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'), bootstrap_servers=KAFKA_BROKERS)
# producer.send(KAFKA_TOPIC, {'foo': 'bar'})
producer.send(KAFKA_TOPIC, value)
