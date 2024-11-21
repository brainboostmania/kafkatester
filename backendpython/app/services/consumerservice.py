from confluent_kafka import Consumer
from validator.errorvalidator import ErrorValidator

class ConsumerService:
    def __init__(self, config):
        self.config = config

    def get_messages(self, data):
        is_success = True
        config = self.config.copy()
        kafka_host = data.get('server').get('kafkaHost')
        config['bootstrap.servers'] = kafka_host
        messages = data.get('messages')
        message_info = []
        errors = []

        for message in messages:
            topic = message.get('topic')
            try:
                consumer = Consumer(config)
                consumer.subscribe([topic])
                print('Consuming topic ' + topic)
                t = 0
                poll_time = 5.0
                while t < 15:
                    msg = consumer.poll(poll_time)
                    if not msg:
                        print('no message yet')
                    elif msg.error():
                        message = 'ERROR: {}'.format(msg.error())
                        print(message)
                        is_success = True
                        break
                    else:
                        message_info.append({
                            'topic': msg.topic(),
                            'key': msg.key().decode('utf-8'),
                            'value': msg.value().decode('utf-8')
                        })
                    t += poll_time
                print('Topic ' + topic + ' consumed')
                consumer.close()
            except Exception as e:
                message = 'Error in getting messages from %s. Error is {}.'.format(topic, e)
                field = 'kafkaServer'
                errors.append({
                    'field': field,
                    'message': message
                })
                break


        output = {
            'success': is_success,
            'message': 'Successful send of message to {}'.format(kafka_host),
            'kafkaMessages': message_info
        }

        output.update(ErrorValidator.process_error(errors))
        return output
