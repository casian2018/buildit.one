<template>
    <Nav />
    <div class="h-full flex flex-col w-full justify-center items-center p-2 px-4 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8 mt-24">
      <div class="w-full mb-4">
        <input
          v-model="searchQuery"
          @input="filterComponents"
          type="text"
          placeholder="Search by category"
          class="w-full p-2 border rounded-md"
        />
      </div>
      <div class="grid gap-8 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 p-4 md:p-2 xl:p-5">
        <!-- Dynamically render components -->
        <div
          v-for="(component, index) in filteredComponents"
          :key="index"
          class="relative bg-white border rounded-lg shadow-md transform transition duration-500 hover:scale-105"
        >
          <div class="absolute top-3 right-3 rounded-full bg-violet-600 text-gray-200 w-6 h-6 text-center">
            {{ index + 1 }}
          </div>
          <div class="p-2 flex justify-center">
            <a :href="component.url">
              <img class="rounded-md" :src="component.imageURL" loading="lazy" />
            </a>
          </div>
          <div class="px-4 pb-3">
            <div>
              <a :href="component.url">
                <h5 class="text-xl font-semibold tracking-tight hover:text-violet-800 text-gray-900">
                  {{ component.title }}
                </h5>
              </a>
              <p class="antialiased text-gray-600 text-sm break-all">
                {{ component.category }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue';
  import { db } from '../firebase'; // Ensure you have the correct path to your Firebase configuration
  import { collection, getDocs } from 'firebase/firestore';
  
  const components = ref([]);
  const searchQuery = ref('');
  
  const fetchComponents = async () => {
    const q = collection(db, 'components');
    const querySnapshot = await getDocs(q);
    components.value = querySnapshot.docs.map(doc => doc.data());
  };
  
  const filteredComponents = computed(() => {
    if (!searchQuery.value) {
      return components.value;
    }
    return components.value.filter(component =>
      component.category.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  });
  
  onMounted(fetchComponents);
  </script>
  
  <style scoped>
  .hidden {
    display: none;
  }
  </style>
  