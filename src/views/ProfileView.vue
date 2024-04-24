<script setup>
import { ref, onMounted } from "vue";
import {useRoute} from "vue-router";
import UserProfileHeader from "../components/UserProfileHeader.vue";
import UserProfilePosts from "../components/UserProfilePosts.vue";

let profile = ref([]);
let posts = ref([])

const route = useRoute();

let userId = route.params.user_id;
const token = localStorage.getItem('jwt_token');


onMounted(() => {
    fetchProfile();
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

</style>