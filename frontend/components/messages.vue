<template>
    <div id="messageContainer">
        <div v-if="items && items.length" class="container text-danger border border-danger rounded bg-danger-subtle">
            <h3>Validation Error</h3>
            <ul>
                <li v-for="item in items">
                    {{ item.message }}
                </li>
            </ul>
        </div>
        <div v-if="message" class="container text-primary border border-primary rounded bg-primary-subtle">
            {{ message }}
        </div>
        <div class="mb-3">&nbsp;</div>
    </div>
</template>

<script setup>
const props = defineProps({
    errorInfo: {
        type: Object,
        required: false,
    },
    successMessage: {
        type: String,
        required: false,
    }
});
const items = props.errorInfo;
const message = props.successMessage;
</script>