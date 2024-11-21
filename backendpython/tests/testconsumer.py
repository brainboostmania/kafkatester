import requests

data = {
    'server': {
        'kafkaHost': 'kafka:29092'
    },
    'messages': [
        {'topic': 'personal-info'},
        {'topic': 'company-info'}
    ]
}
response = requests.post('http://localhost:5000/api/fetch', json=data, verify=False)
print(response.text)