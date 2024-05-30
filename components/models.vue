<template>
  <div
    class="h-full flex w-full justify-center items-center p-2 px-4 mx-auto sm:max-w-xl md:max-w-full lg:max-w-screen-xl md:px-24 lg:px-8"
  >
    <div
      class="grid gap-8 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 p-4 md:p-2 xl:p-5"
    >
      <!-- Dynamically render components -->
      <div
        v-for="(component, index) in components"
        :key="index"
        class="relative bg-white border rounded-lg shadow-md transform transition duration-500 hover:scale-105"
      >
        <div
          class="absolute top-3 right-3 rounded-full bg-violet-600 text-gray-200 w-6 h-6 text-center"
        >
          {{ index + 1 }}
        </div>
        <div class="p-2 flex justify-center">
          <a :href="component.url">
            <img
              class="rounded-md"
              :src="component.imageURL"
              loading="lazy"
            />
          </a>
        </div>

        <div class="px-4 pb-3">
          <div>
            <a :href="component.url">
              <h5
                class="text-xl font-semibold tracking-tight hover:text-violet-800 text-gray-900"
              >
                {{ component.title }}
              </h5>
            </a>

            <p
              class="antialiased text-gray-600 text-sm break-all"
            >
              {{ component.category }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { db } from '../firebase'; // Ensure you have the correct path to your Firebase configuration
import { collection, getDocs, limit, query } from 'firebase/firestore';

const components = ref([]);

const fetchComponents = async () => {
  const q = query(collection(db, 'components'), limit(9));
  const querySnapshot = await getDocs(q);
  components.value = querySnapshot.docs.map(doc => doc.data());
};

onMounted(fetchComponents);
</script>

<style scoped>
.hidden {
  display: none;
}
</style>
