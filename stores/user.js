import { defineStore } from 'pinia';
import { auth } from '~/firebase.js';
import { onAuthStateChanged } from "firebase/auth";

export const useUserStore = defineStore('user', {
  state: () => ({
    user: null,
  }),
  actions: {
    fetchUser() {
      onAuthStateChanged(auth, (user) => {
        if (user) {
          this.user = user;
        } else {
          this.user = null;
        }
      });
    },
    async signOut() {
      await auth.signOut();
      this.user = null;
    }
  }
});
