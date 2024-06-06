<template>
  <div class="flex min-h-screen items-center">
    <div class="max-w-md mx-auto p-4 bg-white rounded-lg shadow-md w-96">
      <h2 class="text-xl font-semibold mb-4">Chat Support</h2>
      <div v-if="!selectedQuestion">
        <label
          for="questions"
          class="block mb-2 text-sm font-medium text-gray-700"
          >Select a question:</label
        >
        <select
          id="questions"
          v-model="selectedQuestion"
          class="block w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
        >
          <option disabled value="">Please select a question</option>
          <option
            v-for="question in questions"
            :key="question.id"
            :value="question"
          >
            {{ question.text }}
          </option>
        </select>
      </div>
      <div v-else>
        <p class="mb-4"><strong>Q:</strong> {{ selectedQuestion.text }}</p>
        <p class="mb-4"><strong>A:</strong> {{ selectedQuestion.answer }}</p>
        <button
          @click="resetSelection"
          class="px-4 py-2 bg-blue-600 text-white rounded-md shadow-sm transition-all duration-150 hover:bg-blue-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600"
        >
          Ask another question
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

const questions = ref([
  {
    id: 1,
    text: "What are your operating hours?",
    answer: "Our operating hours are from 9 AM to 5 PM, Monday to Friday.",
  },
  {
    id: 2,
    text: "How can I track my order?",
    answer:
      'You can track your order by logging into your account and going to the "Orders" section.',
  },
  {
    id: 3,
    text: "What is your return policy?",
    answer:
      "Our return policy allows returns within 30 days of purchase with a receipt.",
  },
]);

const selectedQuestion = ref(null);

const resetSelection = () => {
  selectedQuestion.value = null;
};
</script>
