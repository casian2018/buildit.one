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
          <br /><br />
          Once you've downloaded the initial structure, follow these steps to
          install Node.js:
          <br />
          Visit the official Node.js website at https://nodejs.org/.<br />
          Choose the appropriate installer for your operating system (Windows,
          macOS, or Linux) and download it.<br />
          Run the installer and follow the on-screen instructions to complete
          the installation process.<br />
          After installation, open a terminal or command prompt and type node -v
          to verify that Node.js has been installed correctly. You should see
          the installed version of Node.js displayed in the terminal.<br />
          With Node.js installed, you're now ready to start building and running
          your project using JavaScript on both the client and server sides."<br />
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

    <!-- Step 2: Select Components with Search -->
    <div
      v-if="step === 2"
      class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center"
    >
      <h2 class="font-semibold text-[22px] py-2">Select Components</h2>
      <input
        v-model="searchQuery"
        @input="searchComponents"
        type="text"
        placeholder="Search by category"
        class="mb-4 p-2 border rounded-lg w-96"
      />
      <div class="flex flex-wrap -mx-2 justify-center">
        <button
          v-for="component in filteredComponents"
          :key="component.id"
          @click="toggleSelectComponent(component)"
          class="relative btn mx-2 mb-2"
          :class="{ 'bg-gray-200': isSelected(component) }"
        >
          <div>
            <img :src="component.imageURL" alt="" class="rounded-lg h-96" />
            <p>{{ component.title }}</p>
          </div>
          <span
            v-if="isSelected(component)"
            @click.stop="toggleSelectComponent(component)"
            class="absolute top-0 right-0 bg-red-500 text-white rounded-full w-6 h-6 flex items-center justify-center"
            >X</span
          >
        </button>
      </div>
      <button
        @click="goBackToStepOne"
        class="middle none center mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
      <button
        @click="nextStep"
        class="middle none center mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Continue
      </button>
    </div>

    <!-- Step 3: View and Download Selected Components -->
    <div
      v-if="step === 3"
      class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center"
    >
      <h2 class="font-semibold text-[22px] py-2">Selected Components</h2>
      <div
        v-for="component in selectedComponents"
        :key="component.id"
        class="mt-4 flex flex-col items-center"
      >
        <span class="text-[16px] font-semibold">{{ component.title }}:</span>
        <button
          @click="downloadComponent(component)"
          class="middle none center mt-2 rounded-lg bg-red-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-red-500/20 transition-all hover:shadow-lg hover:shadow-red-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
        >
          Download
        </button>
      </div>
      <button
        @click="nextStep"
        class="middle none center mt-4 rounded-lg bg-yellow-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Host Your Project
      </button>

      <button
        @click="restart"
        class="middle none center mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Restart Project
      </button>
    </div>

    <div
      v-if="step === 4"
      class="bg-white border rounded-lg shadow-md p-4 min-h-64 w-96 flex items-center flex-row justify-center"
    >
      <div class="p-4">
        <h2 class="font-bold">Hosting Instructions</h2>
        <p>
          <strong>Vercel</strong><br /><br />
          Go to Vercel<br /><br />
          Visit the <a href="https://vercel.com" class="underline italic">Vercel website</a> and sign up
          or log in.<br /><br />

          <strong>Create a GitHub Repository</strong><br /><br />
          If you don't already have a GitHub repository for your project, create
          one:<br /><br />
          Go to <a href="https://github.com" class="underline italic">GitHub</a> and log in or sign
          up.<br />
          Click on the "New" button to create a new repository.<br />
          Give your repository a name, add a description if desired, and choose
          whether it should be public or private.<br />
          Click "Create repository".<br /><br />

          <strong>Add Your Project to the GitHub Repository</strong><br /><br />
          On your local machine, open a terminal and navigate to your project
          directory.<br />
          Initialize a new Git repository:<br />
          <code>git init</code><br />
          Add your project files to the repository:<br />
          <code>git add .</code><br />
          Commit the files:<br />
          <code>git commit -m "Initial commit"</code><br />
          Link your local repository to the GitHub repository:<br />
          <code
            >git remote add origin
            https://github.com/yourusername/your-repository-name.git</code
          ><br />
          Push your project to GitHub:<br />
          <code>git push -u origin master</code><br /><br />

          <strong>Import Your GitHub Repository to Vercel</strong><br /><br />
          In Vercel, click on the "New Project" button.<br />
          Select "Import Git Repository".<br />
          Authorize Vercel to access your GitHub account if prompted.<br />
          Find and select your repository from the list.<br />
          Click on "Import".<br /><br />

          <strong>Deploy Your Project</strong><br /><br />
          Follow the steps provided by Vercel to configure your project settings
          if necessary.<br />
          Click on "Deploy" to deploy your project.<br />
          Wait for Vercel to build and deploy your project. Once it's done,
          you'll receive a live URL to access your hosted project.<br />
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from "vue";
import { db } from "../firebase";
import { collection, query, getDocs } from "firebase/firestore";

const step = ref(1);
const components = ref([]);
const selectedComponents = ref([]);
const searchQuery = ref("");
const filteredComponents = ref([]);

const fetchComponents = async () => {
  try {
    const q = query(collection(db, "components"));
    const querySnapshot = await getDocs(q);
    components.value = querySnapshot.docs.map((doc) => ({
      id: doc.id,
      ...doc.data(),
    }));
    searchComponents();
  } catch (error) {
    console.error(`Failed to fetch components: ${error.message}`);
  }
};

const searchComponents = () => {
  if (searchQuery.value) {
    filteredComponents.value = components.value.filter((component) =>
      component.category.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
  } else {
    filteredComponents.value = components.value;
  }
};

watch(searchQuery, searchComponents);

const nextStep = () => {
  step.value++;
  if (step.value === 2) {
    fetchComponents();
  }
};

const toggleSelectComponent = (component) => {
  const index = selectedComponents.value.findIndex(
    (comp) => comp.id === component.id
  );
  if (index === -1) {
    selectedComponents.value.push(component);
  } else {
    selectedComponents.value.splice(index, 1);
  }
};

const isSelected = (component) => {
  return selectedComponents.value.some((comp) => comp.id === component.id);
};

const downloadStructure = () => {
  const link = document.createElement("a");
  link.href =
    "https://data.codeko.ro/raw-aXBmczovL1FtVFFYalI5TWtMekpmN3pidFNqRzRSZDdnTE5RcUc1S3pwclVWOG5lMlo4bUwvbnV4dC56aXA=";
  link.download = "nuxt.zip";
  link.click();
};

const downloadComponent = (component) => {
  const url = component.url;
  if (url) {
    const link = document.createElement("a");
    link.href = url;
    link.download = component.title.replace(/ /g, "_") + ".zip";
    link.click();
  }
};

const goBackToStepOne = () => {
  if (step.value > 1) {
    step.value--;
  }
};

const restart = () => {
  step.value = 1;
  selectedComponents.value = [];
};

onMounted(() => {
  fetchComponents();
});
</script>

<style scoped>
.btn {
  position: relative;
  display: inline-block;
  padding: 8px;
  margin: 4px;
  border: 1px solid #ccc;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #f0f0f0;
}

.btn.selected {
  background-color: #e0e0e0;
}
</style>
