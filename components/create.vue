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
      <div class="flex flex-wrap -mx-2 justify-center justify-center">
        <button @click="selectComponent('Navbar 1')" class="btn mx-2 mb-2">
          <img
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
            class="rounded-lg"
          />
        </button>
        <button @click="selectComponent('Navbar 2')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 3')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 4')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 5')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 6')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 7')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Navbar 8')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Step 3: About Section Selection -->
    <div v-if="step === 3" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold py-2 text-[22px]">Select the About Section</h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button @click="selectComponent('About 1')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 2')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 3')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 4')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 5')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 6')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('About 7')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Step 4: Testimonials Section Selection -->
    <!-- Step 4: Testimonials Section Selection -->
    <div v-if="step === 4" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold py-2 text-[22px]">
          Select the Testimonials Section
        </h2>
      <div class="flex flex-wrap -mx-2 justify-center">
       
        <button
          @click="selectComponent('Testimonials 1')"
          class="btn mx-2 mb-2"
        >
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 2')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 3')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 4')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 5')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 6')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 7')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Testimonials 8')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Step 5: Contact Section Selection -->
    <div v-if="step === 5" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold py-2 text-[22px]">
          Select the Contact Section
        </h2>
      <div class="flex flex-wrap -mx-2 justify-center">
        <button @click="selectComponent('Contact 1')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 2')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 3')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 4')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 5')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 6')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 7')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Contact 8')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Step 6: Footer Section Selection -->
    <div v-if="step === 6" class="bg-white border rounded-lg shadow-md p-4 flex flex-col items-center">
      <h2 class="font-semibold py-2 text-[22px]">
          Select the Footer Section
        </h2>
      <div class="flex flex-wrap -mx-2 justify-center">        
        <button @click="selectComponent('Footer 1')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 2')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 3')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 4')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 5')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 6')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 7')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
        <button @click="selectComponent('Footer 8')" class="btn mx-2 mb-2">
          <img
            class="rounded-lg"
            src="https://tailwindcomponents.com/storage/10609/conversions/temp70025-thumb.jpg"
            alt=""
          />
        </button>
      </div>
      <button
        @click="goBackToStepOne()"
        class="flex justify-center middle none mt-4 rounded-lg bg-blue-500 py-3 px-6 font-sans text-xs font-bold uppercase text-white shadow-md shadow-blue-500/20 transition-all hover:shadow-lg hover:shadow-blue-500/40 focus:opacity-[0.85] focus:shadow-none active:opacity-[0.85] active:shadow-none disabled:pointer-events-none disabled:opacity-50 disabled:shadow-none"
      >
        Back
      </button>
    </div>

    <!-- Step 7: Final Step -->
    <div
      v-if="step === 7"
      class="bg-white border rounded-lg shadow-md p-4 min-h-64 w-96 items-center justify-center"
    >
      <div class="p-4">
        <h2 class="font-semibold py-2 text-[22px]">
          Download Selected Components
        </h2>
        <!-- Display components and download buttons -->
        <div v-for="component in components" :key="component.name" class="mt-4">
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
        <p class="my-4">Would you like to make other project ?</p>
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
      v-if="step === 8"
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

const step = ref(1);
const components = ref([]);

const componentUrls = {
  "Navbar 1": "https://example.com/navbar1.zip",
  "Navbar 2": "https://example.com/navbar2.zip",
  "Navbar 3": "https://example.com/navbar3.zip",
  "Navbar 4": "https://example.com/navbar4.zip",
  "Navbar 5": "https://example.com/navbar5.zip",
  "Navbar 6": "https://example.com/navbar6.zip",
  "Navbar 7": "https://example.com/navbar7.zip",
  "Navbar 8": "https://example.com/navbar8.zip",
  "Hero 1": "https://example.com/hero1.zip",
  "Hero 2": "https://example.com/hero2.zip",
  "Hero 3": "https://example.com/hero3.zip",
  "Hero 4": "https://example.com/hero4.zip",
  "Hero 5": "https://example.com/hero5.zip",
  "Hero 6": "https://example.com/hero6.zip",
  "Hero 7": "https://example.com/hero7.zip",
  "Hero 8": "https://example.com/hero8.zip",
  "About 1": "https://example.com/about1.zip",
  "About 2": "https://example.com/about2.zip",
  "About 3": "https://example.com/about3.zip",
  "About 4": "https://example.com/about4.zip",
  "About 5": "https://example.com/about5.zip",
  "About 6": "https://example.com/about6.zip",
  "About 7": "https://example.com/about7.zip",
  "About 8": "https://example.com/about8.zip",
  "Testimonials 1": "https://example.com/testimonials1.zip",
  "Testimonials 2": "https://example.com/testimonials2.zip",
  "Testimonials 3": "https://example.com/testimonials3.zip",
  "Testimonials 4": "https://example.com/testimonials4.zip",
  "Testimonials 5": "https://example.com/testimonials5.zip",
  "Testimonials 6": "https://example.com/testimonials6.zip",
  "Testimonials 7": "https://example.com/testimonials7.zip",
  "Testimonials 8": "https://example.com/testimonials8.zip",
  "Contact 1": "https://example.com/contact1.zip",
  "Contact 2": "https://example.com/contact2.zip",
  "Contact 3": "https://example.com/contact3.zip",
  "Contact 4": "https://example.com/contact4.zip",
  "Contact 5": "https://example.com/contact5.zip",
  "Contact 6": "https://example.com/contact6.zip",
  "Contact 7": "https://example.com/contact7.zip",
  "Contact 8": "https://example.com/contact8.zip",
  "Footer 1": "https://example.com/footer1.zip",
  "Footer 2": "https://example.com/footer2.zip",
  "Footer 3": "https://example.com/footer3.zip",
  "Footer 4": "https://example.com/footer4.zip",
  "Footer 5": "https://example.com/footer5.zip",
  "Footer 6": "https://example.com/footer6.zip",
  "Footer 7": "https://example.com/footer7.zip",
  "Footer 8": "https://example.com/footer8.zip",
};

const nextStep = () => {
  step.value++;
};

const selectComponent = (component) => {
  components.value.push({ name: component }); // Store components with names
  nextStep();
};

const downloadStructure = () => {
  // Logic to download the initial structure
  const link = document.createElement("a");
  link.href =
    "https://data.codeko.ro/raw-aXBmczovL1FtVHl3UGZVeDNTQzRkRWozdVZlanM4dEtxZWlQeUR6Sld0TlhSdGhQMTdVZXgvbnV4dC56aXA=";
  link.download = "initial-structure.zip";
  link.click();
};

const downloadComponent = (component) => {
  const url = componentUrls[component];
  if (url) {
    const link = document.createElement("a");
    link.href = url;
    link.download = component.replace(/ /g, "_") + ".zip"; // Replacing spaces with underscores
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
  if (step.value > 1) {
    step.value = 1;
  }
}
</script>
