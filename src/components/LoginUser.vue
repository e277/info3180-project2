<template>
    <div class="container-login">
        <div class="card w-30">
            <div class="card-body">
                <p class="card-text">
                    <h3 class="text-center mb-4">Login</h3>
                    <form @submit.prevent="login">
                        <div class="mb-3">
                            <label for="username" class="form-label">Username</label>
                            <input type="text" v-model="username" class="form-control border-login" id="username" required>
                        </div>
                        <div class="mb-3">
                            <label for="password" class="form-label">Password</label>
                            <input type="password" v-model="password" class="form-control border-login" id="password" required>
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
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const username = ref('');
const password = ref('');

const login = async () => {
  try {
    const response = await fetch('/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        username: username.value,
        password: password.value
      })
    });
    const data = await response.json();
    if (response.ok) {
      alert(data.message);
      router.push('/');
    } else {
      alert(data.message);
    }
  } catch (error) {
    console.error('Login failed:', error);
    alert('Login failed. Please try again later.');
  }
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