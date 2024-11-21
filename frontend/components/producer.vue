<template>
  <div>
    <messages ref="msg" v-if="hasProducerError" :errorInfo="producerError" :successMessage="successMessage"></messages>
    <div class="card">
      <div class="card-header">
        Server Info
      </div>
      <div class="card-body">
        <div class="mb-3">
          <label for="serverUrl" class="form-label">Server URL</label>
          <input type="text" class="form-control" id="serverUrl" v-model="serverUrl" />
        </div>
      </div>
    </div>

    <div class="mb-3">&nbsp;</div>

    <div class="card">
      <div class="card-header">
        Message Details
      </div>
      <div class="card-body">
        <div class="mb-3">
          <label for="topic" class="form-label">Topic</label>
          <input type="text" class="form-control" id="topic" v-model="topic" />
        </div>
        <div class="mb-3">
          <label for="messageType" class="form-label">Message Type</label>
          <select class="form-select" id="messageType" aria-label="Default select example" v-model="messageType"
            @change="changeType">
            <option selected>Select type</option>
            <option value="string">String</option>
            <option value="number">Number</option>
            <option value="json">JSON</option>
          </select>
        </div>
        <div class="mb-3">
          <label for="messageId" class="form-label">Message ID</label>
          <input type="text" class="form-control" id="messageId" v-model="messageId" />
        </div>
        <div class="mb-3">
          <label for="message" class="form-label">Message</label>
          <textarea class="form-control" id="message" rows="5" v-model="message"></textarea>
        </div>
      </div>
    </div>

    <div class="mb-3">&nbsp;</div>
    <div class="mb-3">
      <button @click="submitEntry" type="button" class="btn btn-primary">Submit</button>
    </div>
  </div>
</template>

<script setup>
const serverUrl = useState('serverUrl');
const topic = useState('topic');
const message = useState('message');
const messageType = useState('messageType');
const messageId = useState('messageId');
let hasProducerError = ref(false);
let producerError = ref([]);
let successMessage = ref('');
let msg = ref('msg');

function clearFields() {
  serverUrl.value = '';
  topic.value = '';
  message.value = '';
  messageType.value = '';
  messageId.value = '';
}


async function submitEntry() {
  const data = {
    'server': {
      'kafkaHost': serverUrl.value
    },
    'messages': [
      {
        'topic': topic.value,
        'key': messageId.value,
        "messageType": messageType.value,
        'value': message.value
      },
    ]
  }

  await $fetch('/api/send', {
    method: 'POST',
    body: data
  }).then(response => {
    const isError = response.success == false;
    hasProducerError.value = isError;
    producerError = response.errors;
    successMessage.value = response.message;
    if (!isError) clearFields();
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
  })
}


</script>