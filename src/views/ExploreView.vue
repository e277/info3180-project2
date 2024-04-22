<script setup>
import { ref } from "vue";
import FeedPost from "../components/FeedPost.vue";


</script>

<template>
    <div class="pageWrapper">
        
        <FeedPost :profilePic="`profile${index}.jpg`"  v-for="index in 5" :key="index"/>
    </div>
   
</template>

<style>

.pageWrapper{
    padding: 50px 30px;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
  
</style>