import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider, signInWithPopup, createUserWithEmailAndPassword, signInWithEmailAndPassword } from "firebase/auth";
import { getFirestore, addDoc } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyBHLPpFpqjNDQsS5WFy0JoW13i6OnuTnCg",
  authDomain: "buildit-bc6eb.firebaseapp.com",
  projectId: "buildit-bc6eb",
  storageBucket: "buildit-bc6eb.appspot.com",
  messagingSenderId: "792534239374",
  appId: "1:792534239374:web:3b48e47a23dcdade7d21df",
  measurementId: "G-NF66DGTXJY"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();

export { app, db, addDoc, auth, googleProvider, signInWithPopup, createUserWithEmailAndPassword, signInWithEmailAndPassword };
