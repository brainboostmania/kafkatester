from .errorvalidator import ErrorValidator


class ProducerValidator(ErrorValidator):

    def validate(self, data):
        errors = []
        server_info = data.get('server')
        messages = data.get('messages')
        self.add_error(errors, self.validate_kafka_url(server_info))
        self.add_error(errors, self.validate_topic(messages))
        self.add_error(errors, self.validate_key(messages))
        self.add_error(errors, self.validate_value(messages))
        return self.process_error(errors)

    @staticmethod
    def validate_key(messages) -> dict | None:
        for msg in messages:
            if not msg.get('key'):
                return {
                    'field': 'message id',
                    'message': 'One of the messages has no message id'
                }
        return None

    @staticmethod
    def validate_value(messages) -> dict | None:
        for msg in messages:
            if not msg.get('value'):
                return {
                    'field': 'message',
                    'message': 'One of the messages has no value for the message'
                }
        return None