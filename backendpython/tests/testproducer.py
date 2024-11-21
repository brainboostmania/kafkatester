import requests

data = {
    'server': {
        'kafkaHost': 'kafka:29092'
    },
    'messages': [
        {
            'topic': 'personal-info',
            'key': 'person',
            'value': {
                'name': 'John Doe',
                'address1': 'Ayala Ave',
                'city': 'Makati',
                'province' : 'Metro Manila'
            }
        },
        {
            'topic': 'personal-info',
            'key': 'name',
            'value': 'Jane Dee'
        },
        {
            'topic': 'personal-info',
            'key': 'age',
            'value': 25
        },
        {
            'topic': 'company-info',
            'key': 'email',
            'value': 'mail@mail.com'
        },
    ]
}

response = requests.post('http://localhost:5000/api/send', json=data, verify=False)
print(response.text)