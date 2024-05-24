<template>
  <div>
    <Nav />
    <div class="py-16">
      <div
        class="flex bg-white rounded-lg shadow-lg overflow-hidden mx-auto max-w-sm lg:max-w-4xl"
      >
        <div
          class="hidden lg:block lg:w-1/2 bg-cover"
          :style="{
            backgroundImage:
              'url(https://images.unsplash.com/photo-1546514714-df0ccc50d7bf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=667&q=80)',
          }"
        ></div>
        <div class="w-full p-8 lg:w-1/2">
          <h2 class="text-2xl font-semibold text-gray-700 text-center">
            Brand
          </h2>
          <p class="text-xl text-gray-600 text-center">Create your account</p>
          <a
            @click="registerWithGoogle"
            class="flex items-center justify-center mt-4 text-white rounded-lg shadow-md hover:bg-gray-100 cursor-pointer"
          >
            <div class="px-4 py-3">
              <svg class="h-6 w-6" viewBox="0 0 40 40">
                <!-- SVG paths for Google logo -->
              </svg>
            </div>
            <h1 class="px-4 py-3 w-5/6 text-center text-gray-600 font-bold">
              Sign up with Google
            </h1>
          </a>
          <div class="mt-4 flex items-center justify-between">
            <span class="border-b w-1/5 lg:w-1/4"></span>
            <a href="#" class="text-xs text-center text-gray-500 uppercase"
              >or sign up with email</a
            >
            <span class="border-b w-1/5 lg:w-1/4"></span>
          </div>
          <div class="mt-4">
            <label class="block text-gray-700 text-sm font-bold mb-2"
              >Email Address</label
            >
            <input
              v-model="email"
              class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
              type="email"
            />
          </div>
          <div class="mt-4">
            <div class="flex justify-between">
              <label class="block text-gray-700 text-sm font-bold mb-2"
                >Password</label
              >
            </div>
            <input
              v-model="password"
              class="bg-gray-200 text-gray-700 focus:outline-none focus:shadow-outline border border-gray-300 rounded py-2 px-4 block w-full appearance-none"
              type="password"
            />
          </div>
          <div class="mt-8">
            <button
              @click="register"
              class="bg-gray-700 text-white font-bold py-2 px-4 w-full rounded hover:bg-gray-600"
            >
              Sign Up
            </button>
          </div>
          <div v-if="error" class="mt-4 text-red-600 text-center">
            {{ error }}
          </div>
        </div>
      </div>
    </div>
    <Footer />
  </div>
</template>

<script setup>
import { ref } from "vue";
import {
  auth,
  googleProvider,
  signInWithPopup,
  createUserWithEmailAndPassword,
} from "../firebase.js";


const email = ref("");
const password = ref("");
const error = ref("");

const registerWithGoogle = async () => {
  try {
    const result = await signInWithPopup(auth, googleProvider);
    const user = result.user;


    window.location.href = `/profile/${user.uid}`;
  } catch (err) {
    if (err.code === "auth/account-exists-with-different-credential") {
      error.value = "You already have an account. Please login.";
    } else {
      error.value = err.message;
    }
  }
};

const register = async () => {
  try {
    const result = await createUserWithEmailAndPassword(
      auth,
      email.value,
      password.value
    );

    window.location.href = `/login`;
  } catch (err) {
    if (err.code === "auth/email-already-in-use") {
      error.value = "You already have an account. Please login.";
    } else {
      error.value = err.message;
    }
  }
};
</script>

<style scoped>
.hidden {
  display: none;
}
</style>
