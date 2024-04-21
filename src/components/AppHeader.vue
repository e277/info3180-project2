<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
      <div class="container-fluid">
        <a class="navbar-brand" href="/"></a>
        <span class="navbar-brand"><img src="../assets/cam.png" alt="Photogram Logo" width="30" height="30" class="d-inline-block align-top">Photogram</span>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/">MyProfile</RouterLink>
            </li>
            <li class="nav-item" v-if="loggedin">
              <RouterLink class="nav-link active" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref,reactive } from "vue";

const loggedin = true;

const loginState = reactive({
  loggedin :false
});

function checkstatus(){
  const auth = localStorage.getItem('token');
  loginState.loggedin = auth != null;
}

checkstatus();


</script>

<style>
    .container-fluid{
        display:flex;
        flex-direction:row;
    }
    
    img {
        width: 40px;
        height: auto;
    }
    
    nav{
        background-color: #5c95ff;
        color:white;
    }
    
    span{
        margin:5px;
        font-size:40px;
        font-family: "Papyrus","Lucida Handwriting","Lucida Console";
    }
    
    RouterLink{
        font-family: "Verdana", "Courier New", monospace;
        font-size:20px;
    }
    
    .navbar-nav{
        display: flex;
        flex-direction: row;
        list-style-type: none;
        padding-left: 400px;
    }

    .navbar-brand,
    .navbar-text,
    .navbar-toggler {
        display: inline-flex;
        align-items: center;
        margin-right:1px;

    }
</style>