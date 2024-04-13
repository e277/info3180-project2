<script setup>
import { ref } from "vue";
</script>

<template>
    <div class="homesquares">
        <img src="uploads/wallpaper.jpeg" alt="Photogram Logo" width="30" height="30" class="home1">
        <div class = "information">
            <span class="navbar-brand"><img src="uploads/cam.png" alt="Photogram Logo" width="30" height="30" class="d-inline-block align-top">Photogram</span>
            <hr>
            <p>Share photos of your favourite moments with friends, family and the world.</p>
            <div class ="options">
                <button>Register</button>
                <button>Login</button>
            </div>
        </div>
    </div>
</template>

<style>
    .homesquares{
        display:flex;
        flex-direction:row;
        margin:60px;
        padding:30px;
    }
    
    .home1{
        width:530px;
        height:360px;
        border: 1px solid grey;
        margin:20px;
        box-shadow: 10px 10px 5px #aaaaaa;
        border-radius: 10px;
    }
    
    .information{
        width:500px;
        height:300px;
        margin:20px;
        padding:30px;
        border: 1px solid grey;
        box-shadow: 10px 10px 5px #aaaaaa;
        border-radius: 10px;
        background-color:#FFF8EB;
    }
    
    .navbar-brand {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .options{
        padding:20px;
        margin:20px;
    }
    
    button{
        width:190px;
        height:40px;
    }
    
    .reg{
        background-color:#049C12;
        margin:10px;
        border-radius: 5px;
        color:white;
        font-size:20px;
        font-family: "Verdana", "Courier New", monospace;
    }
    
    .log{
        background-color:#9c048e;
        border-radius: 5px;
        color:white;
        font-size:20px;
        font-family: "Verdana", "Courier New", monospace;
    }
    
    p{
        font-size:18px;
        font-family: "Verdana", "Courier New", monospace;
    }
</style>