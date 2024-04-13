<template>
    <h1>New Post</h1>
    <form @submit.prevent = "saveMovie" id="movieForm" class = "movie-form">
        <div class="form-group mb-3">
            <label for="poster" class="form-label">Photo</label>
            <br>
            <input type="file" @change="onFileChange" id="poster" name="poster" class="form-control" accept="image/*"/>
        </div>
        <div class="form-group mb-3">
            <br>
            <label for="description" class="form-label">Caption</label>
            <br>
            <input v-model="mData.description" id="description" name="description" class="form-control2" placeholder="Write a caption..."/>
        </div>
            <br>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
</template>

<script setup>

</script>


<style>
form{
        background-color:#FFF8EB;
        margin-left:400px;
        padding:30px;
        display: flex;
        flex-direction: column;
        width:500px;
        height:350px;
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
        width:500px;
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
        width:500px;
        font-size:20px;
        color:white;
        background-color:#7dbb13;
        border: 1px solid #7dbb13;
        border-radius: 5px;
    }
   
</style>
