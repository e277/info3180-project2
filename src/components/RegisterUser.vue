<template>
    <div class="entire-page">
        <h3>Register</h3>
        <form class="container mt-4" @submit.prevent="registerUser" id="registerForm">
             <div class="card w-50">
                <div class="card-body">
                    <p class="card-text">
                        <div class="mb-3">
                            <label for="username" class="form-label bold">Username</label>
                            <input type="text" class="form-control border1" name="username" v-model="username" required>
                        </div>    
                        <div class="mb-3">          
                            <label for="password" class="form-label bold">Password</label>
                            <input type="password" name="password" class="form-control border1" aria-describedby="passwordHelpBlock" v-model="password" required>
                        </div>  
                        <div class="mb-3">
                            <label for="firstname" class="form-label bold">First Name</label>
                            <input type="text" class="form-control border1" name="firstname" v-model="firstname" required>
                        </div>
                        <div class="mb-3">
                            <label for="lastname" class="form-label bold">Last Name</label>
                            <input type="text" class="form-control border1" name="lastname" v-model="lastname" required>
                        </div>
                        <div class="mb-3">
                            <label for="email" class="form-label bold">Email</label>
                            <input type="email" class="form-control border1" name="email" placeholder="name@example.com" v-model="email" required>
                        </div>
                        <div class="mb-3">
                            <label for="location" class="form-label bold">Location</label>
                            <input type="text" class="form-control border1" name="location" v-model="location" required>
                        </div>
                        <div class="mb-3">
                            <label for="biography" class="form-label bold">Biography</label>
                            <textarea class="form-control border1" name="biography" rows="3" v-model="biography" required></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="profile_photo" class="form-label bold">Photo</label>
                            <input class="form-control border1" type="file" id="profile_photo" name="profile_photo" @change="handleFileUpload" accept="image/*" required>
                        </div>

                        <button type="submit" class="btn btn-primary btn-block">Register</button>
                    </p>
                </div>
            </div>        
        </form>    
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import router from '../router/index.js';

const username = ref('');
const password = ref('');
const firstname = ref('');
const lastname = ref('');
const email = ref('');
const location = ref('');
const biography = ref('');
const profile_photo = ref(null);

let csrf_token = ref("")

onMounted(() => {
  getCsrfToken();
})

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log(data);
        csrf_token.value = data.csrf_token;
    })
    .catch(error => console.error('Error fetching CSRF token:', error));
  }

function registerUser() {
    let registerForm = document.getElementById('registerForm');
    let userData = new FormData(registerForm);

    fetch('/api/v1/register', {
        method: 'POST',
        body: userData,
        headers: {
            'X-CSRFToken': csrf_token.value
        }        
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Registration failed.');
        }
        return response.json();
    })
    .then(function (data) { 
        console.log(data);
        alert("Registration successful!");
        router.push('/profile/' + data.user_id);
    })
    .catch(function (error){
        console.log(error);
        alert("Registration failed.");
        router.push('/register');
    });
}

function handleFileUpload(event){
    const file = event.target.files[0];
    if (file){
        profile_photo.value = file;
    }
}

</script>


<style scoped>
.container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
}

h3 {
    text-align: center;
    padding-top: 20px;
    font-family:'Times New Roman', Times, serif;
    font-weight: bold;
}

.card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    border-color: black;   
    background-color: white; 
    padding: 20px;
    margin-bottom: 40px;
}

.entire-page {
    background-color: #fff8eb;
}

.btn-block {
    width: 100%;
}

.bold {
    font-weight: bold;
    font-family:'Times New Roman', Times, serif;
}

.border1 {
    border-color: black;
    font-family:'Times New Roman', Times, serif;
}
</style>