<script setup>
import { ref, onMounted } from "vue";
import FeedPost from "../components/FeedPost.vue";
import { Plus } from 'lucide-vue-next';
import { useRouter } from 'vue-router';

const router = useRouter();
let allPosts = ref([]);

const token = localStorage.getItem('jwt_token');

onMounted(() => {
    //if(token != "undefined"){
        
        fetchPosts();
    // }else{
    //     router.push('/login');
    // }
    
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
        allPosts.value = data.posts; 
    })
    .catch(error => {
        console.error(error);
    });
}
</script>

<template>
    <div class="pageWrapper">
        
        <div class="ctn">

            <div class="addNew">
                <a href="/post/create">
                    <Plus size="24" stroke-width="2.75" />
                    New Post
                </a>
            </div>

            <FeedPost v-for="post in allPosts" :key="post.user_id"
                :id="post.id"
                :userId="post.user_id"
                :profilePic="post.profile_pic"
                :username="post.username"
                :photo="post.photo" 
                :caption="post.caption"
                :date="post.created_on"
                :likes="post.likes"
                :isLiked="post.isLiked"
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

.ctn{
    position: relative;
}

.addNew{
    color: #fff;
    background-color: #1a1a1a;
    max-width: fit-content;
    border-radius: 100px;
    text-transform: uppercase;
    font-weight: 800;
    font-size: 0.75rem;
    position: fixed;
    top: 125px;
    right: 216px;

   
}

.addNew:hover{
    background-color: #0f6cf6;
    cursor: pointer; 
}

.addNew a{
    all: unset;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0.4rem 1rem;
}

</style>
