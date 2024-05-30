import { useUserStore } from '/stores/user.js';

export default defineNuxtPlugin((nuxtApp) => {
  const userStore = useUserStore();
  userStore.fetchUser();
});
