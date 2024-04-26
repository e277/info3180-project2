<template>
  <header v-if="loaded">
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">

      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <span class="navbar-brand"><img src="../assets/cam.png" alt="Photogram Logo" width="30" height="30" class="d-inline-block align-top">Photogram</span>
        </a>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active">Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" :to="link">MyProfile</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link active" to="/logout">Logout</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>


import { ref, onMounted, watchEffect } from "vue";
import { useRouter } from "vue-router";


const router = useRouter();
const loaded = ref(false);
const link = ref();

const token = ref();
token.value = localStorage.getItem('jwt_token');


function setLink(){
  if (token && token != "undefined") {
    link.value = '/profile/' + localStorage.getItem('user_id');
    // link.value = '/profile/' + 2;
    loaded.value = true;
  } else {
    loaded.value = true;
    router.push('/login');
  }
}

onMounted(() => {
  link.value = '/profile/' + localStorage.getItem('user_id');
  loaded.value = true;
  setLink();

});

// watchEffect(() => {
//   followersCount.value = props.followersCount;
//   isFollowing.value = props.isFollowing;
// });



</script>

<style>
    header{
      position: relative;
    }
    .container-fluid{
        display:flex;
        flex-direction:row;
    }

    .container-fluid a{
      width:190px;
      text-align:center;
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

    .signinMessage{
      position: absolute;
      top: 100px;
      left: 100px;
      background-color: #1a1a1a;
      padding: 0.5rem 0.9rem;
      border-radius: 100px;

    }
</style>