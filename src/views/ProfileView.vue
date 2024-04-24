<script setup>
import { ref } from "vue";

let profile = ref([]);

// const userId = localStorage.getItem('user_id');  TODO: uncomment
let userId = 4;
const token = localStorage.getItem('jwt_token');


onMounted(() => {
    fetchProfile();
})

function fetchProfile() {
    fetch(`/api/v1/users/${userId}/posts`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        profile.value = data.posts; 
        console.log(data)
    })
    .catch(error => {
        console.error(error);
    });

}

</script>

<template>
    <div class="pageWrapper">
    </div>
</template>

<style>

</style>