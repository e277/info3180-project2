<template>
    <div class="container-login">
        <div class="card w-30">
            <div class="card-body">
                <p class="card-text">
                    <h3 class="text-center mb-4">Login</h3>
                    <form @submit.prevent="login" id="loginForm">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" v-model="username" class="form-control border-login" name="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" v-model="password" class="form-control border-login" name="password" required>
                        </div>
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary">Login</button>
                        </div>
                    </form>
                </p>
            </div>
        </div>
    </div>
</template>


<script setup>
import { ref, onMounted } from 'vue';
import router from '../router/index.js'; 

const username = ref('');
const password = ref('');

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
        csrf_token.value = data;
    })
  };

function login() {
  let loginForm = document.getElementById('loginForm');
  let userData = new FormData(loginForm);

  fetch('/api/v1/auth/login', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrf_token,
      'Authorization': 'Bearer ' + localStorage.getItem('token')
    },
    body: userData,
  })
  .then(response => {
    if (!response.ok) {
        console.log(response.errors);
      //throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    console.log(data);
    localStorage.setItem('token', data.token);
    alert(data.message);
    router.push('/');
  })
  .catch(error => {
    console.log(error);
    alert(error.message);
    router.push('/login');
  });
};
</script>

<style scoped>
.container-login {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #fff8eb;
}

.card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
    border-color: black;   
    background-color: white; 
    padding: 20px;
    margin-bottom: 40px;
    font-weight: bold;
    margin-top: -150px;
}

h3 {
    font-weight: bold;
    font-family: 'Times New Roman', Times, serif;
}

.border-login {
    border-color: black;
}

.btn {
    background-color: #7dbb13;
}

.mb-3 {
    font-family: 'Times New Roman', Times, serif;
}

.text-center button {
    font-family: 'Times New Roman', Times, serif;
}

</style>