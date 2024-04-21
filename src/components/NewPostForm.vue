<template>
    <form @submit.prevent = "savePost" id="postForm" class = "post-form">
        <div class="form-group mb-3">
            <label for="photo" class="form-label">Photo</label>
            <br>
            <input type="file" @change="onFileChange" id="poster" name="poster" class="form-control" accept="image/*"/>
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

const pData = ref({
    caption:'',
    photo: null,
});

function savePost() {

    let postForm = document.getElementById('postForm');
    let form_data = new FormData(postForm);
    let user_id = current_user.user_id;

    fetch("/api/v1/users/"+user_id+"/posts", {
        method: 'POST',
        body: form_data,
    })
    .then(function (response){
        return response.json();
    })
    .then(function (data) { 
        console.log(data);       
    })
    .catch(function (error){
        console.log(error);
    });
};

function onFileChange(event){
    const file = event.target.files[0];
    if (file){
        pData.value.poster = file;
    }
}

</script>


<style>
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
