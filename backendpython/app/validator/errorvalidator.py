import validators
from abc import ABC, abstractmethod


class ErrorValidator:

    @staticmethod
    def validate_kafka_url(data) -> dict | None:
        url = data.get('kafkaHost')
        if not url:
            return {
                'field': 'kafkaHost',
                'message': 'KAFKA URL must be supplied'
            }
        return None

    @staticmethod
    def validate_topic(messages) -> dict | None:
        for msg in messages:
            if not msg.get('topic'):
                return {
                    'field': 'topic',
                    'message': 'One of the messages has no topic'
                }

        return None

    @staticmethod
    def add_error(errors: list, error: dict):
        if error:
            errors.append(error)

    @staticmethod
    def process_error(errors: list):
        if len(errors) > 1:
            return {
                'success': False,
                'errors': errors
            }

        return {
            'success': True,
        }
