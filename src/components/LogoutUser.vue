<template>
    <div class="container-logout">
        <div class="card w-30">
            <div class="card-body">
                <p class="card-text">
                    <h3 class="text-center mb-4">Logout</h3>
                    <div class="text-center">
                        <p>Are you sure you want to logout?</p>
                        <button @click="cancel" class="btn btn-secondary me-3">Cancel</button>
                        <button @click="logout" class="btn btn-primary btn-logout">Logout</button>
                    </div>
                </p>
            </div>
        </div>
    </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const logout = async () => {
  try {
    const response = await fetch('/api/v1/auth/logout', {
      method: 'POST',
    });
    if (response.ok) {
      router.push({ path: '/login' });
    } else {
      console.error('Logout failed:', response.statusText);
      alert('Logout failed. Please try again later.');
    }
  } catch (error) {
    console.error('Logout failed:', error);
    alert('Logout failed. Please try again later.');
  }
};

const cancel = () => {
  router.push({ path: '/' });
};
</script>

<style scoped>
.container-logout {
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

.text-center{
    font-family: 'Times New Roman', Times, serif;
}

.text-center p{
    font-family: 'Times New Roman', Times, serif;
}

</style>