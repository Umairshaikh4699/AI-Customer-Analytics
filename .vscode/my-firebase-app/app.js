// app.js (module)
import { initializeApp } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-auth.js";
import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-firestore.js";
import { getStorage, ref as storageRef, uploadBytes, getDownloadURL } from "https://www.gstatic.com/firebasejs/12.5.0/firebase-storage.js";

// ---- your firebaseConfig (use your values) ----
const firebaseConfig = {
  apiKey: "AIzaSyBeR5HgAOqb2MyFxf23lnsu5A0vvBMHuE4",
  authDomain: "studio-8244632068-6e8bb.firebaseapp.com",
  projectId: "studio-8244632068-6e8bb",
  storageBucket: "studio-8244632068-6e8bb.firebasestorage.app",
  messagingSenderId: "461333484774",
  appId: "1:461333484774:web:64ec4a372899a587e05727"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const db = getFirestore(app);
const storage = getStorage(app);

// UI elements
const emailEl = document.getElementById('email');
const passEl = document.getElementById('password');
const signupBtn = document.getElementById('signup');
const loginBtn = document.getElementById('login');
const logoutBtn = document.getElementById('logout');
const appDiv = document.getElementById('app');
const userEmailSpan = document.getElementById('userEmail');
const addDocBtn = document.getElementById('addDoc');
const fileInput = document.getElementById('fileInput');
const uploadBtn = document.getElementById('upload');

// Auth: Sign up
signupBtn.addEventListener('click', async () => {
  try {
    const userCred = await createUserWithEmailAndPassword(auth, emailEl.value, passEl.value);
    alert('Signed up: ' + userCred.user.email);
  } catch (err) {
    alert('Signup error: ' + err.message);
  }
});

// Auth: Log in
loginBtn.addEventListener('click', async () => {
  try {
    await signInWithEmailAndPassword(auth, emailEl.value, passEl.value);
    alert('Logged in');
  } catch (err) {
    alert('Login error: ' + err.message);
  }
});

// Auth: Log out
logoutBtn.addEventListener('click', async () => {
  await signOut(auth);
});

// React to auth state
onAuthStateChanged(auth, user => {
  if (user) {
    appDiv.style.display = 'block';
    userEmailSpan.textContent = user.email;
  } else {
    appDiv.style.display = 'none';
    userEmailSpan.textContent = '';
  }
});

// Firestore: Add a doc
addDocBtn.addEventListener('click', async () => {
  try {
    const docRef = await addDoc(collection(db, 'samples'), {
      createdAt: new Date(),
      note: 'Hello from client'
    });
    alert('Doc added: ' + docRef.id);
  } catch (err) {
    alert('Add doc error: ' + err.message);
  }
});

// Storage: Upload file
uploadBtn.addEventListener('click', async () => {
  const file = fileInput.files[0];
  if (!file) return alert('Choose a file first');
  const ref = storageRef(storage, `uploads/${Date.now()}_${file.name}`);
  try {
    await uploadBytes(ref, file);
    const url = await getDownloadURL(ref);
    alert('Uploaded. File URL: ' + url);
  } catch (err) {
    alert('Upload error: ' + err.message);
  }
});
