<script setup>
import { ref } from "vue";
</script>

<template>
    <div class="homesquares">
            <img src="../assets/wallpaper.jpeg" alt="Photogram Logo" width="30" height="30" class="home1">
            <div class = "information">
                <span class="navbar-brand"><img src="../assets/cam.png" alt="Photogram Logo" width="30" height="30" class="d-inline-block align-top">Photogram</span>
                <hr>
                <p>Share photos of your favourite moments with friends, family and the world.</p>
                <div class ="options">
                    <a href="/register" class="reg">Register</a>
                    <a href="/login" class="log">Login</a>
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
      height:360px;
      margin:20px;
      padding:30px;
      border: 1px solid #ccc;
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
      display: flex;
      justify-content: row;
  }
        
  a{
    width:190px;
    height:40px;
    text-align:center;
  }
        
  .reg{
      background-color:#7dbb13;
      margin:10px;
      border-radius: 5px;
      color:white;
      font-size:20px;
      font-family: "Verdana", "Courier New", monospace;
      border: 1px solid #7dbb13;
      text-decoration:none;
  }
        
  .log{
      background-color:#5013BB;
      border-radius: 5px;
      margin:10px;
      color:white;
      font-size:20px;
      font-family: "Verdana", "Courier New", monospace;
      border: 1px solid #5013BB;
      text-decoration:none;
  }
        
  p{
      font-size:18px;
      font-family: "Verdana", "Courier New", monospace;
  }
</style>