<script setup>
import { ref, onMounted } from "vue";
import {useRoute} from "vue-router";
import UserProfileHeader from "../components/UserProfileHeader.vue";
import UserProfilePosts from "../components/UserProfilePosts.vue";
import { Images } from "lucide-vue-next";

let profile = ref([]);
let posts = ref([])

const route = useRoute();

let userId = route.params.user_id;
const token = localStorage.getItem('jwt_token');


onMounted(() => {
    if (!localStorage.getItem('jwt_token')) {
    route.push('/login');
    }   
    else{
    fetchProfile();
    } 
})

function fetchProfile() {
    fetch(`/api/v1/users/${userId}/posts`, {
        method: 'GET',
        headers: {
            'Authorization': `Bearer ${token}`
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        posts.value = data.posts; 
        profile.value = data.user_info; 
    })
    .catch(error => {
        console.error(error);
    });

}

</script>

<template>
    <div class="pageWrapper">

        <div class="profileCtn">

            <UserProfileHeader
                :id="profile.id"
                :firstname="profile.firstname"
                :lastname="profile.lastname"
                :location="profile.location"
                :joinedOn="profile.joined_on"
                :profilePic="profile.profile_photo"
                :bio="profile.bio"
                :followersCount="profile.followers_count"
                :totalPosts="profile.total_posts"
                :isFollowing="profile.isFollowing"
            
            />

            <div v-if="posts.length == 0" class="no-posts-yet-ctn">
                <Images size="100" stroke-width="1.3"/>
                
                Hmmm.... seems like this user doesn't have any posts yet
            
            </div>

            <div class="postGrid">

                <UserProfilePosts v-for="post in posts" :key="post.id"

                    :id="post.id"
                    :photo="post.photo"
                
                />

            </div>
        </div>
    </div>
</template>

<style>

.profileCtn{
    width: 100%;
    max-width: 1300px;
}

.postGrid{
    display: grid;
    grid-template-columns: repeat(3, 1fr); 
    grid-gap: 7px; 
}

.no-posts-yet-ctn{
    display: flex;
    width: 100%;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    color: rgb(147, 161, 164);
}

</style>