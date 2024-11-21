<template>
  <div>
    <messages ref="msg" v-if="hasConsumerError" :errorInfo="consumerError" :successMessage="successMessage"></messages>
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
          <label for="topics" class="form-label">Topics</label>
          <input type="text" class="form-control" id="topics" v-model="topics" />
        </div>
      </div>
    </div>

    <div class="mb-3">&nbsp;</div>
    <div class="mb-3">
      <button @click="submitEntry" type="button" class="btn btn-primary">Submit</button>
    </div>

    <table class="table border">
      <thead>
        <tr>
          <th scope="col">Topic</th>
          <th scope="col">Message ID</th>
          <th scope="col">Message</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items">
          <td>{{ item.topic }}</td>
          <td>{{ item.key }}</td>
          <td>{{ item.value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
const serverUrl = useState('serverUrl');
const topics = useState('topics');
let items = ref([]);
let hasConsumerError = ref(false);
let successMessage = ref('');
let consumerError = ref([]);

function clearFields() {
  serverUrl.value = '';
  topics.value = '';
}

async function submitEntry() {
  let messages = [];
  const searchTopics = topics.value?.split(',');
  for (const topic in searchTopics) {
    messages.push({'topic': searchTopics[topic].trim()})
  }

  const data = {
    'server': {
      'kafkaHost': serverUrl.value
    },
    'messages': messages
  }
  items.value = []

  await $fetch('/api/fetch', {
    method: 'POST',
    body: data
  }).then(response => {
    const isError = response.success == false;
    hasConsumerError.value = isError;
    consumerError = response.errors;
    successMessage.value = response.message
    items.value = response.kafkaMessages || [];
    if (!isError) clearFields();
    window.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
  })
}


</script>