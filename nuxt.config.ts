// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: ["@nuxtjs/tailwindcss", '@pinia/nuxt'],
  plugins: [
    '~/plugins/initUser.js'
  ],
})