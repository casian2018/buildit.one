<template>
  <Nav />

  <div class="max-w-md mx-auto p-4 bg-white shadow-md rounded-lg my-48">
    <h1 class="text-2xl font-bold mb-4">Add New Component</h1>
    <form @submit.prevent="addComponent">
      <div class="mb-4">
        <label for="category" class="block text-sm font-medium text-gray-700"
          >Category</label
        >
        <select
          type="text"
          id="category"
          v-model="category"
          class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
        >
          <option value="button" :value="Navbar">Navbar</option>
          <option value="card" :value="Hero">Hero</option>
          <option value="form" :value="Contact">Contact</option>
          <option value="input" :value="Form">Form</option>
          <option value="table" :value="Table">Table</option>
          <option value="modal" :value="Footer">Footer</option>
          <option value="about" :value="About">About</option>
        </select>
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
        <label for="url" class="block text-sm font-medium text-gray-700"
          >URL</label
        >
        <input
          type="text"
          id="url"
          v-model="url"
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
const url = ref("");
const imageURL = ref("");
const uid = ref("");

// Function to add a new component to Firestore
const addComponent = async () => {
  try {
    await addDoc(collection(db, "components"), {
      category: category.value,
      title: title.value,
      url: url.value,
      imageURL: imageURL.value,
      uid: uid.value,
    });
    alert("Component added successfully!");
    // Clear form fields
    category.value = "";
    title.value = "";
    url.value = "";
    imageURL.value = "";
    uid.value = "";
  } catch (error) {
    console.error("Error adding component: ", error);
    alert("Error adding component");
  }
};
</script>

<style scoped>
/* Optional: Add any additional styles here */
</style>
