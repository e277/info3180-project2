<template>
    <form @submit.prevent = "savePost" id="postForm" class = "post-form" enctype="multipart/form-data">
        <input type="hidden" id="user_id" name="user_id" class="form-control"/>
        <div class="form-group mb-3">
            <label for="photo" class="form-label">Photo</label>
            <br>
            <input type="file" @change="onFileChange" id="photo" name="photo" class="form-control" accept="image/*"/>
        </div>
        <div class="form-group mb-3">
            <br>
            <label for="caption" class="form-label">Caption</label>
            <br>
            <input v-model="pData.caption" id="caption" name="caption" class="form-control2" placeholder="Write a caption..."/>
        </div>
            <br>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
</template>

<script setup>

import { ref, onMounted } from "vue";
import router from '../router/index.js';

const pData = ref({
    caption:'',
    photo: null,
});

const csrf_token = ref("")

onMounted(() => {
    if (!localStorage.getItem('jwt_token')) {
        router.push('/login');
    }

    getCsrfToken();
})

function getCsrfToken() {
    fetch('/api/v1/csrf-token')
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        // console.log(data);
        csrf_token.value = data.csrf_token;
    })
};

function savePost() {
    const token = localStorage.getItem('jwt_token');
    const user_id = localStorage.getItem('user_id');  // Retrieve user ID from local storage

    let form_data = new FormData();
    form_data.append("photo", pData.value.photo);
    form_data.append("caption", pData.value.caption);
    form_data.append("user_id", user_id);

    fetch("/api/v1/users/"+user_id+"/posts", {
        method: 'POST',
        body: form_data,
        headers: {
            'X-CSRFToken': csrf_token.value,
            'Authorization': 'Bearer ' + token
        }
    })
    .then(function (response){
        return response.json();
    })
    .then(function (data) { 
        console.log(data);
        alert("Post submitted successfully!");      
    })
    .catch(function (error){
        console.log(error);
        alert("Failed to submit post.");
    });
};

function onFileChange(event){
    const file = event.target.files[0];
    if (file){
        pData.value.photo = file;
    }
}

</script>


<style scoped>
form{
    background-color:#FFF8EB;
    margin-left:400px;
    padding:30px;
    display: flex;
    flex-direction: column;
    width:500px;
    height:auto;
    font-size:30px;
    border: 1px solid #BFBFBF;
    box-shadow: 10px 10px 5px #aaaaaa;
    border-radius: 10px;
}

h1{
    margin-left:400px;
    padding-top:30px;
}

.form-control2{
    width:400px;
    height:70px;
    font-size:16px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

.form-control{
    font-size:16px;
    color:grey;
}

button{
    height:50px;
    width:400px;
    font-size:20px;
    color:white;
    background-color:#7dbb13;
    border: 1px solid #7dbb13;
    border-radius: 5px;
}

</style>
