from confluent_kafka import Producer
from validator.errorvalidator import ErrorValidator

class ProducerService:

    def __init__(self, config):
        self.config = config

    def delivery_callback(self, err, msg):
        if err:
            print('ERROR: Message failed delivery: {}'.format(err))
        else:
            print('Produced event to topic {topic}: key = {key:12} value = {value:12}'.format(
                topic=msg.topic(), key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))

    def send_message(self, data: dict):
        config = self.config.copy()
        kafka_host = data.get('server').get('kafkaHost')
        config['bootstrap.servers'] = kafka_host
        messages = data.get('messages')
        errors = []

        try:
            producer = Producer(config)
            for message in messages:
                topic = message.get('topic')
                value = message.get('value')
                key = message.get('key')
                producer.produce(topic, str(value), key, callback=self.delivery_callback)

            producer.poll(10000)
            producer.flush()

        except Exception as e:
            message = 'Error in sending message. Error is {}.'.format(e)
            field = 'kafkaServer'
            errors.append({
                'field': field,
                'message': message
            })

        output = ErrorValidator.process_error(errors)
        output['message'] = 'Successful send of message to {}'.format(kafka_host)
        return output