<template>
  <section class="w-full h-screen mx-auto flex">
    <div class="lg:w-[80%] md:w-[90%] sm:w-[92%] xs:w-[96%] mx-auto flex items-center justify-center">
      <div class="w-full md:p-6 xs:p-4 rounded-lg md:mt-0 sm:p-8">
        <div class="w-full mx-auto shadow-xl rounded-sm border border-gray-200">
          <h1 class="text-2xl font-semibold p-4 bg-gray-200 shadow-lg rounded-sm">Profile</h1>
          <div class="flex items-center justify-center min-h-screen bg-gray-100">
            <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
              <div class="step-content" id="step1">
                <!-- Step 1 Content -->
                <div class="w-full mb-4">
                  <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900">First Name</label>
                  <input v-model="profileData.first_name" type="text" name="first_name" id="first_name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" required />
                </div>
                <div class="w-full mb-4">
                  <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900">Last Name</label>
                  <input v-model="profileData.last_name" type="text" name="last_name" id="last_name" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" required />
                </div>
                <div class="w-full mb-4">
                  <label for="email" class="block mb-2 text-sm font-medium text-gray-900">Email</label>
                  <input v-model="profileData.email" type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" required />
                </div>
                <div class="w-full mb-4">
                  <label for="phone_no" class="block mb-2 text-sm font-medium text-gray-900">Phone Number</label>
                  <input v-model="profileData.phone_no" type="text" name="phone_no" id="phone_no" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5" required />
                </div>
                <div class="w-full flex justify-between p-2 bg-gray-200">
                  <button @click="previousStep" class="sm:px-8 xs:px-4 py-2 bg-blue-400 text-white rounded-lg">Previous</button>
                  <button @click="saveProfile" class="sm:px-8 xs:px-4 py-2 bg-blue-700 text-white rounded-lg">Save</button>
                  <button @click="nextStep" class="sm:px-8 xs:px-4 py-2 bg-blue-700 text-white rounded-lg">Next</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, getDoc, setDoc } from 'firebase/firestore';

export default {
  setup() {
    const auth = getAuth();
    const db = getFirestore();
    
    const user = ref(null);
    const isLoading = ref(false);
    const profileData = ref({
      first_name: '',
      last_name: '',
      email: '',
      phone_no: ''
    });

    onAuthStateChanged(auth, async (currentUser) => {
      if (currentUser) {
        user.value = currentUser;
        isLoading.value = true;
        try {
          const userRef = doc(db, 'users', currentUser.uid);
          const userSnap = await getDoc(userRef);
          if (userSnap.exists()) {
            profileData.value = { ...profileData.value, ...userSnap.data() };
          } else {
            console.error('User profile not found');
          }
        } catch (error) {
          console.error('Error fetching user profile:', error);
        } finally {
          isLoading.value = false;
        }
      } else {
        user.value = null;
        profileData.value = {
          first_name: '',
          last_name: '',
          email: '',
          phone_no: ''
        };
      }
    });

    const saveProfile = async () => {
      if (user.value) {
        try {
          const userRef = doc(db, 'users', user.value.uid);
          await setDoc(userRef, profileData.value, { merge: true });
          alert('Profile saved successfully!');
        } catch (error) {
          console.error('Error saving profile:', error);
        }
      }
    };

    const previousStep = () => {
      // Handle previous step logic here
    };

    const nextStep = () => {
      // Handle next step logic here
    };

    return {
      user,
      isLoading,
      profileData,
      saveProfile,
      previousStep,
      nextStep
    };
  },
};
</script>

<style scoped>
/* Add any custom styles here */
</style>
