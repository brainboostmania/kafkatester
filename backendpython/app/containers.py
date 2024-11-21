from dependency_injector import containers, providers

from validator.producervalidator import ProducerValidator
from validator.consumervalidator import ConsumerValidator
from services.producerservice import ProducerService
from services.consumerservice import ConsumerService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration(yaml_files=['config.yml'])
    producer_config = {
        'acks': 'all'
    }

    consumer_config = {
        'group.id': 'kafka-python-getting-started',
        'auto.offset.reset': 'earliest'
    }


class Services(containers.DeclarativeContainer):
    producer_service = providers.Factory(ProducerService, Container.producer_config)
    consumer_service = providers.Factory(ConsumerService, Container.consumer_config)


class Validator(containers.DeclarativeContainer):
    producer_validator = providers.Factory(ProducerValidator)
    consumer_validator = providers.Factory(ConsumerValidator)
