<template>
  <div class="container mx-auto py-8">
    <div class="flex justify-center items-center h-screen min-h-screen min-w-screen" v-if="step === 1">
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

    <div v-if="step === 2">
      <h1 class="text-3xl font-bold mb-6">Document Queue</h1>
      <div class="mb-6">
        <h2 class="text-2xl font-bold">Inserted Documents</h2>
        <ul class="list-disc ml-6">
          <li v-for="insertedDoc in insertedDocs" :key="insertedDoc.id">
            {{ insertedDoc.name }}
          </li>
        </ul>
      </div>
      <div
        v-for="doc in docs"
        :key="doc.id"
        class="border p-4 mb-4 rounded-lg shadow-lg"
      >
        <p>{{ doc.data().name }}</p>
        <p>{{ doc.data().content }}</p>
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
</template>

<script setup>
import { ref, onMounted } from "vue";
import {
  db,
  collection,
  getDocs,
  addDoc,
  deleteDoc,
  doc,
  getDoc,
} from "../firebase";
import { sendAuthCodeToDiscord } from "../utils/discord";

const code = ref("");
const errorMessage = ref("");
const step = ref(1);  // Variable to manage the authentication step

const insertedDocs = ref([]); // Store inserted documents
const docs = ref([]); // Store documents from Firebase

const verifyCode = async () => {
  try {
    const querySnapshot = await getDocs(collection(db, "authCodes"));
    const codes = querySnapshot.docs.map((doc) => doc.data().code);

    if (codes.includes(code.value)) {
      // Authentication successful
      step.value++;
      fetchDocs();  // Fetch documents after successful authentication
    } else {
      errorMessage.value = "Invalid code. Please try again.";
    }
  } catch (error) {
    console.error("Error verifying code:", error);
    errorMessage.value = "An error occurred. Please try again later.";
  }
};

const fetchDocs = async () => {
  try {
    const querySnapshot = await getDocs(collection(db, "queue"));
    docs.value = querySnapshot.docs;
  } catch (error) {
    console.error("Error fetching documents:", error);
  }
};

const approveDoc = async (id) => {
  try {
    const docRef = doc(db, "queue", id);
    const docSnap = await getDoc(docRef);

    if (docSnap.exists()) {
      const docData = docSnap.data();
      await addDoc(collection(db, "components"), docData);
      await deleteDoc(docRef);
      insertedDocs.value.push({ id, name: docData.name }); // Add to insertedDocs
      fetchDocs();
    }
  } catch (error) {
    console.error("Error approving document:", error);
  }
};

const rejectDoc = async (id) => {
  try {
    await deleteDoc(doc(db, "queue", id));
    fetchDocs();
  } catch (error) {
    console.error("Error rejecting document:", error);
  }
};

onMounted(async () => {
  // Generate and send authentication code to Discord on component mount
  const authCode = Math.random().toString(36).substring(2, 8).toUpperCase();
  await addDoc(collection(db, "authCodes"), { code: authCode });
  await sendAuthCodeToDiscord(authCode);
});
</script>
