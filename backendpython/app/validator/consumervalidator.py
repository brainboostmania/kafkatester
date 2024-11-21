from .errorvalidator import ErrorValidator


class ConsumerValidator(ErrorValidator):

    def validate(self, data):
        errors = []
        server_info = data.get('server')
        messages = data.get('messages')
        self.add_error(errors, self.validate_kafka_url(server_info))
        self.add_error(errors, self.validate_topic(messages))
        return self.process_error(errors)
