<script setup>
import { ref, onMounted } from "vue";
import FeedPost from "../components/FeedPost.vue";

let allPosts = ref([]);

const token = localStorage.getItem('jwt_token');

onMounted(() => {
    fetchPosts();
})

function fetchPosts() {
    fetch("/api/v1/posts", {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        allPosts.value = data.posts; // Assign the posts data directly to allPosts.value
    })
    .catch(error => {
        console.error(error);
    });
}
</script>

<template>
    <div class="pageWrapper">
        
        <div class="ctn">
            <FeedPost v-for="post in allPosts" :key="post.username"
                :profilePic="post.profile_pic"
                :username="post.username"
                :photo="post.photo" 
                :caption="post.caption"
                :date="post.created_on"
                :likes="post.likes"
            />
        </div>
    </div>
</template>

<style>
.pageWrapper {
    padding: 50px 30px;
    width: 100vw;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f9faf9;
    
}

</style>
