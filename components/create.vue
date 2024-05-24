<template>
  <div
    class="p-3 md:p-4 xl:p-5 flex min-h-screen items-center align-middle justify-center mt-24"
  >
    <!-- Step 1: Initial Download and Continue -->
    <div
      v-if="step === 1"
      class="bg-white border rounded-lg shadow-md p-4 min-h-64 w-96 flex items-center flex-row justify-center"
    >
      <div class="p-4">
        <p class="font-semibold py-2 text-[22px]">
          Download the initial structure:
        </p>
        <p class="pb-2">
          Downloading the initial structure involves acquiring the foundational
          files and resources needed to kickstart your project. Additionally,
          you'll need to install Node.js, a JavaScript runtime environment, to
          execute JavaScript code outside of a web browser. Node.js is essential
          for building and running server-side applications, enabling developers
          to leverage its vast ecosystem of libraries and tools for efficient
          development.
          <br />
          <br />
          Once you've downloaded the initial structure, follow these steps to
          install Node.js:
          <br />
          <br />
          Visit the official Node.js website at
          <a href="https://nodejs.org/" class="underline">https://nodejs.org/</a
          >.
          <br />
          Choose the appropriate installer for your operating system (Windows,
          macOS, or Linux) and download it.
          <br />
          Run the installer and follow the on-screen instructions to complete
          the installation process.
          <br />
          After installation, open a terminal or command prompt and type node -v
          to verify that Node.js has been installed correctly. You should see
          the installed version of Node.js displayed in the terminal.
          <br />
          With Node.js installed, you're now ready to start building and running
          your project using JavaScript on both the client and server sides."
        </p>
        <button
          @click="downloadStructure"
          class="middle none center mr-4 rounded-lg bg-red-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-red-500/20 transition-all hover:shadow-lg hover:shadow-red-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        >
          Download
        </button>
        <button
          @click="nextStep"
          class="middle none center mr-4 rounded-lg bg-green-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-green-500/20 transition-all hover:shadow-lg hover:shadow-green-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        >
          Continue
        </button>
      </div>
    </div>

    <!-- Step 2: Navbar Selection -->
    <div v-if="step === 2" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Navbar</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <div v-if="step === 3" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Hero</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <div v-if="step === 4" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a About</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <div v-if="step === 5" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Contact</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>
    <div v-if="step === 6" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Footer</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <div v-if="step === 7" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Table</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <div v-if="step === 8" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold text-[22px] py-2">Select a Form</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button v-for="component in components" :key="component.name" @click="selectComponent(component.name)" class="btn mx-2 mb-2">
          <img :src="component.thumbnail" alt="" class="rounded-lg" />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Steps 3-6 follow the same structure as Step 2 with different component categories -->

    <!-- Step 7: Final Step -->
    <div
      v-if="step === 9"
      class="bg-white border rounded-lg shadow-md p-4 min-h-64 w-96 items-center justify-center"
    >
      <div class="p-4">
        <h2 class="font-semibold py-2 text-[22px]">
          Download Selected Components
        </h2>
        <!-- Display components and download buttons -->
        <div v-for="component in selectedComponents" :key="component.name" class="mt-4">
          <span class="text-[16px] font-semibold">{{ component.name }}:</span>
          <br />
          <button
            @click="downloadComponent(component.name)"
            class="middle none center mr-4 rounded-lg bg-red-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-red-500/20 transition-all hover:shadow-lg hover:shadow-red-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
          >
            Download
          </button>
        </div>
        <p class="mt-4">How to add components to your project:</p>
        <!-- Add images and text instructions here -->
        <p class="mt-4">
          After downloading the components, place them in your Nuxt project's
          components folder and import them as needed.
        </p>
        <p class="my-4">Would you like to host the project?</p>
        <button
          @click="hostProject"
          class="middle none center rounded-lg bg-orange-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-orange-500/20 transition-all hover:shadow-lg hover:shadow-orange-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        >
          Host Project
        </button>
        <p class="my-4">Would you like to make another project?</p>
        <button
          @click="restart()"
          class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        >
          Restart Project
        </button>
      </div>
    </div>

    <!-- Step 8: Hosting Instructions -->
    <div
      v-if="step === 10"
      class="bg-white border rounded-lg shadow-md p-4 min-h-64 w-96 flex items-center flex-row justify-center"
    >
      <div class="p-4">
        <h2>Hosting Instructions</h2>
        <p>Here is how you can host your project:</p>
        <h3>Vercel</h3>
        <ul>
          <li>
            Go to
            <a href="https://vercel.com" target="_blank" class="text-blue-500"
              >Vercel</a
            >
            and sign up or log in.
          </li>
          <li>Import your GitHub repository to Vercel.</li>
          <li>Follow the steps to deploy your project.</li>
        </ul>
        <h3>Adding to Discord</h3>
        <ul>
          <li>
            Create a new application on the
            <a
              href="https://discord.com/developers/applications"
              target="_blank"
              class="text-blue-500"
              >Discord Developer Portal</a
            >.
          </li>
          <li>Set up a bot and invite it to your server.</li>
          <li>
            Use the bot to share your project link with your server members.
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const step = ref(1);
const components = ref([]);
const selectedComponents = ref([]);
const category = ref("");

const fetchComponents = async (category) => {
  // Replace with actual database call
  const response = await fetch(`/api/components?category=${category}`);
  const data = await response.json();
  components.value = data;
};

const nextStep = () => {
  step.value++;
  if (step.value > 1 && step.value < 7) {
    setCategoryForStep(step.value);
    fetchComponents(category.value);
  }
};

const selectComponent = (component) => {
  selectedComponents.value.push({ name: component });
  nextStep();
};

const downloadStructure = () => {
  // Logic to download the initial structure
  const link = document.createElement("a");
  link.href = "https://example.com/initial-structure.zip";
  link.download = "initial-structure.zip";
  link.click();
};

const downloadComponent = (component) => {
  const url = components.value.find(comp => comp.name === component).downloadUrl;
  if (url) {
    const link = document.createElement("a");
    link.href = url;
    link.download = component.replace(/ /g, "_") + ".zip";
    link.click();
  }
};

const hostProject = () => {
  nextStep();
};

function goBackToStepOne() {
  if (step.value > 1) {
    step.value--;
  }
}

function restart() {
  step.value = 1;
  selectedComponents.value = [];
}

function setCategoryForStep(step) {
  switch (step) {
    case 2:
      category.value = "navbar";
      break;
    case 3:
      category.value = "hero";
      break;
    case 4:
      category.value = "about";
      break;
    case 5:
      category.value = "contact";
      break;
    case 6:
      category.value = "footer";
      break;
      case 7:
      category.value = "table";
      break;
      case 8:
      category.value = "form";
      break;
    default:
      category.value = "";
  }
}

onMounted(() => {
  fetchComponents("navbar");
});
</script>
