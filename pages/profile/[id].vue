<template>
  <section class="w-full h-screen mx-auto flex ">
    <div
      class="lg:w-[80%] md:w-[90%] sm:w-[92%] xs:w-[96%] mx-auto flex items-center justify-center"
    >
      <div
        class="w-full md:p-6 xs:p-4 rounded-lg md:mt-0 sm:p-8 "
      >
        <!--  -->
        <div
          class="w-full mx-auto shadow-xl rounded-sm border border-gray-200 "
        >
          <h1
            class="text-2xl font-semibold p-4 bg-gray-200 shadow-lg   rounded-sm"
          >
            Profile
          </h1>

          <!-- Steps -->
          <div class="w-full md:flex sm:gap-2 xs:gap-0">
            <div
              class="lg:w-[20%] md:w-[30%] xs:w-full bg-gray-100 flex md:flex-col xs:flex-row xs:justify-center sm:gap-2"
            >
              <div
                class="step-tab text-gray-900 rounded-sm py-2 sm:bg-gray-400  xs:bg-blue-500 border-b-2 border-gray-200 -b-2 -gray-600 pl-4 hover:bg-gray-400 hover:text-white"
                data-step="1"
              >
                <div
                  class="flex md:gap-2 sm:text-xl xs:text-md font-semibold  cursor-pointer"
                >
                  Step -
                  <h1
                    class="md:text-3xl xs:text-lg sm:text-white flex justify-center sm:px-2 xs:pr-2 xs:bg-blue-500 rounded-lg"
                  >
                    1
                  </h1>
                </div>
              </div>
              <div
                class="step-tab rounded-sm py-2 border-b-2 border-gray-200 -b-2 -gray-600 pl-4 hover:bg-gray-400 hover:text-white "
                data-step="2"
              >
                <div
                  class="flex md:gap-2 sm:text-xl xs:text-md font-semibold  cursor-pointer"
                >
                  Step -
                  <h1
                    class="md:text-3xl xs:text-lg sm:text-white flex justify-center sm:px-2 sm:bg-blue-500 rounded-lg"
                  >
                    2
                  </h1>
                </div>
              </div>
              <div
                class="step-tab rounded-sm py-2 border-b-2 border-gray-200 -b-2 -gray-600 pl-4 hover:bg-gray-400 hover:text-white "
                data-step="3"
              >
                <div
                  class="flex md:gap-2 sm:text-xl xs:text-md font-semibold  cursor-pointer"
                >
                  Step -
                  <h1
                    class="md:text-3xl xs:text-lg sm:text-white flex justify-center sm:px-2 sm:bg-blue-500 rounded-lg"
                  >
                    3
                  </h1>
                </div>
              </div>
              <div
                class="step-tab rounded-sm py-2 border-b-2 border-gray-200 -b-2 -gray-600 pl-4 hover:bg-gray-400 hover:text-white "
                data-step="4"
              >
                <div
                  class="flex md:gap-2 sm:text-xl xs:text-md font-semibold  cursor-pointer"
                >
                  Step -
                  <h1
                    class="md:text-3xl xs:text-lg sm:text-white flex justify-center sm:px-2 sm:bg-blue-500 rounded-lg"
                  >
                    4
                  </h1>
                </div>
              </div>
            </div>

            <!-- Step contents -->
            <div class="md:w-[88%] xs:w-[92%] px-4 py-6">
              <div class="step-content" id="step1">
                <!-- Step 1 Content -->
                <div class="w-full">
                  <label
                    for="first_name"
                    class="block mb-2 text-sm font-medium text-gray-900 "
                    >First Name</label
                  >
                  <input
                    type="text"
                    name="first_name"
                    id="first_name"
                    class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  -gray-600 "
                    required
                  />
                </div>
                <div class="w-full">
                  <label
                    for="last_name"
                    class="block mb-2 text-sm font-medium text-gray-900 "
                    >Last Name</label
                  >
                  <input
                    type="text"
                    name="last_name"
                    id="last_name"
                    class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  -gray-600  "
                    required
                  />
                </div>
                <div class="w-full">
                  <label
                    for="email"
                    class="block mb-2 text-sm font-medium text-gray-900 "
                    >Email</label
                  >
                  <input
                    type="email"
                    name="email"
                    id="email"
                    class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  -gray-600  "
                    required
                  />
                </div>
                <div class="w-full">
                  <label
                    for="phone_no"
                    class="block mb-2 text-sm font-medium text-gray-900 "
                    >Phone Number</label
                  >
                  <input
                    type="text"
                    name="phone_no"
                    id="phone_no"
                    class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5  -gray-600  "
                    required
                  />
                </div>
              </div>
              <div class="step-content hidden" id="step2">
                <!-- Step 2 Content -->
                <p class="text-gray-900 ">
                  Step 2 content goes here...
                </p>
              </div>
              <div class="step-content hidden" id="step3">
                <!-- Step 3 Content -->
                <p class="text-gray-900 ">
                  Step 3 content goes here...
                </p>
              </div>
              <div class="step-content hidden" id="step4">
                <!-- Step 4 Content -->
                <p class="text-gray-900 ">
                  Step 4 content goes here...
                </p>
              </div>
            </div>
          </div>

          <div
            class="w-full flex justify-between p-2 bg-gray-200 "
          >
            <button
              class="sm:px-8 xs:px-4 py-2 bg-blue-400 text-white rounded-lg"
            >
              Previous
            </button>
            <button
              type="submit"
              class="sm:px-8 xs:px-4 py-2 bg-blue-700 text-white rounded-lg"
            >
              Next
            </button>
          </div>
        </div>
        <!--  -->
      </div>
    </div>
  </section>
</template>

<script>
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { getFirestore, doc, getDoc } from 'firebase/firestore';

export default {
  setup() {
    const auth = getAuth();
    const db = getFirestore();

    const user = ref(null);
    const isLoading = ref(false);
    const profileData = ref({});

    onAuthStateChanged(auth, (currentUser) => {
      if (currentUser) {
        user.value = currentUser;
        isLoading.value = true;
        const userRef = doc(db, 'users', currentUser.uid);
        getDoc(userRef)
          .then((userSnap) => {
            if (userSnap.exists) {
              profileData.value = userSnap.data();
            } else {
              console.error('User profile not found');
            }
          })
          .finally(() => {
            isLoading.value = false;
          });
      } else {
        user.value = null;
        profileData.value = {};
      }
    });

    return {
      user,
      isLoading,
      profileData,
    };
  },
};
</script>