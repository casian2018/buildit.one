<template>
  <div class="container mx-auto py-8">
    <div v-if="!authenticated" class="flex justify-center items-center h-screen min-h-screen min-w-screen">
      <div class="text-center">
        <h1 class="text-2xl font-bold mb-4">Enter the Authentication Code</h1>
        <input
          v-model="code"
          type="text"
          placeholder="Enter code"
          class="border p-2 rounded mb-4"
        />
        <button
          @click="verifyCode"
          class="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Verify
        </button>
        <p v-if="errorMessage" class="text-red-500 mt-4">{{ errorMessage }}</p>
      </div>
    </div>

    <div v-if="authenticated">
      <h1 class="text-3xl font-bold mb-6">Document Queue</h1>
      <div class="grid gap-8 grid-cols-1 sm:grid-cols-2 md:grid-cols-3 p-4 md:p-2 xl:p-5">
        <div
          v-for="doc in docs"
          :key="doc.id"
          class="relative bg-white border rounded-lg shadow-md transform transition duration-500 hover:scale-105"
        >
          <div class="absolute top-3 right-3 rounded-full bg-violet-600 text-gray-200 w-6 h-6 text-center">
            {{ doc.index + 1 }}
          </div>
          <div class="p-2 flex justify-center">
            <img class="rounded-md" :src="doc.data().imageURL" alt="Document Image" loading="lazy" />
          </div>
          <div class="px-4 pb-3">
            <div>
              <h5 class="text-xl font-semibold tracking-tight text-gray-900">
                {{ doc.data().title }}
              </h5>
              <p class="antialiased text-gray-600 text-sm break-all">
                {{ doc.data().content }}
              </p>
            </div>
            <div class="flex justify-end space-x-4 mt-4">
              <button
                @click="approveDoc(doc.id)"
                class="bg-green-500 text-white px-4 py-2 rounded"
              >
                Approve
              </button>
              <button
                @click="rejectDoc(doc.id)"
                class="bg-red-500 text-white px-4 py-2 rounded"
              >
                Reject
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { db } from '../firebase'; // Ensure this path is correct
import { collection, getDocs, addDoc, deleteDoc, doc, getDoc } from 'firebase/firestore';
import { sendAuthCodeToDiscord } from '../utils/discord';

const code = ref('');
const errorMessage = ref('');
const authenticated = ref(false);
const docs = ref([]);

const verifyCode = async () => {
  try {
    const querySnapshot = await getDocs(collection(db, 'authCodes'));
    const codes = querySnapshot.docs.map((doc) => doc.data().code);

    if (codes.includes(code.value)) {
      authenticated.value = true;
      fetchDocs();
    } else {
      errorMessage.value = 'Invalid code. Please try again.';
    }
  } catch (error) {
    console.error('Error verifying code:', error);
    errorMessage.value = 'An error occurred. Please try again later.';
  }
};

const fetchDocs = async () => {
  try {
    const querySnapshot = await getDocs(collection(db, 'queue'));
    docs.value = querySnapshot.docs.map((doc, index) => ({
      id: doc.id,
      index,
      data: doc.data()
    }));
  } catch (error) {
    console.error('Error fetching documents:', error);
  }
};

const approveDoc = async (id) => {
  try {
    const docRef = doc(db, 'queue', id);
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const docData = docSnap.data();
      await addDoc(collection(db, 'components'), docData);
      await deleteDoc(docRef);
      fetchDocs();
    }
  } catch (error) {
    console.error('Error approving document:', error);
  }
};

const rejectDoc = async (id) => {
  try {
    await deleteDoc(doc(db, 'queue', id));
    fetchDocs();
  } catch (error) {
    console.error('Error rejecting document:', error);
  }
};

onMounted(async () => {
  const authCode = Math.random().toString(36).substring(2, 8).toUpperCase();
  await addDoc(collection(db, 'authCodes'), { code: authCode });
  await sendAuthCodeToDiscord(authCode);
});
</script>

<style scoped>
.hidden {
  display: none;
}
</style>
