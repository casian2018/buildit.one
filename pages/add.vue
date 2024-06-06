<template>
  <Nav />

  <div class="max-w-md mx-auto p-4 bg-white shadow-md rounded-lg my-48">
    <h1 class="text-2xl font-bold mb-4">Add New Component</h1>
    <form @submit.prevent="addComponent">
      <div class="mb-4">
        <label for="category" class="block text-sm font-medium text-gray-700"
          >Category</label
        >
        <input
          type="text"
          id="category"
          v-model="category"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        />
      </div>
      <div class="mb-4">
        <label for="title" class="block text-sm font-medium text-gray-700"
          >Title</label
        >
        <input
          type="text"
          id="title"
          v-model="title"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        />
      </div>
      <div class="mb-4">
        <label for="title" class="block text-sm font-medium text-gray-700"
          >Tailwind</label
        >
        <select
          type="text"
          id="tailwind"
          v-model="tailwind"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        >
        <option value="tailwind">Yes</option>
        <option value="CSS">No</option>
        </select>
      </div>
      <div class="mb-4">
        <label for="url" class="block text-sm font-medium text-gray-700"
          >Code</label
        >
        <input
          type="text"
          id="code"
          v-model="code"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        />
      </div>
      <div class="mb-4">
        <label for="imageURL" class="block text-sm font-medium text-gray-700"
          >Image URL</label
        >
        <input
          type="text"
          id="imageURL"
          v-model="imageURL"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        />
      </div>
      <div class="mb-4">
        <label for="imageURL" class="block text-sm font-medium text-gray-700"
          >User ID</label
        >
        <input
      type="text"
      id="uid"
      v-model="uid"
      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
      readonly
    />
      </div>
      <div>
        <button
          type="submit"
          class="bg-blue-500 text-white py-2 px-4 rounded-md shadow-sm hover:bg-blue-600"
        >
          Add Component
        </button>
      </div>
    </form>
  </div>

  <Footer />
</template>

<script setup>
import { ref } from "vue";
import { collection, addDoc } from "firebase/firestore";
import { db } from "~/firebase.js";
// Form data
const category = ref("");
const title = ref("");
const tailwind = ref("");
const code = ref("");
const imageURL = ref("");
// Function to add a new component to Firestore
const addComponent = async () => {
  try {
    await addDoc(collection(db, "quene"), {
      category: category.value,
      title: title.value,
      tailwind: tailwind.value,
      code: code.value,
      imageURL: imageURL.value,
      uid: uid.value,
    });
    alert("Component added successfully!");
    // Clear form fields
    category.value = "";
    title.value = "";
    tailwind.value = "";
    code.value = "";
    imageURL.value = "";
    uid.value = "";
  } catch (error) {
    console.error("Error adding component: ", error);
    alert("Error adding component");
  }
};




import { computed } from 'vue';
import { useUserStore } from '~/stores/user.js';

const userStore = useUserStore();
const uid = computed(() => userStore.user?.uid || '');
</script>

<style scoped>
/* Optional: Add any additional styles here */
</style>