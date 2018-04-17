from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:1234')
for _ in range(100):
     producer.send('Retrieve', b'Person.csv')
# Block until a single message is sent (or timeout)
future = producer.send('Retrieve', b'Last_Name.json')
result = future.get(timeout=60)
# Block until all pending messages are at least put on the network
# NOTE: This does not guarantee delivery or success! It is really
# only useful if you configure internal batching using linger_ms
producer.flush()
# Use a key for hashed-partitioning
producer.send('York', key=b'Retrieve', value=b'Run')
# Serialize json messages
import json
producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))
producer.send('Retrieve', {'Retrieve': 'Run'})
# Serialize string keys
producer = KafkaProducer(key_serializer=str.encode)
producer.send('Retrieve', key='ping', value=b'1234')
# Compress messages
producer = KafkaProducer(compression_type='gzip')
for i in range(1000):
     producer.send('Retrieve', b'msg %d' % i)