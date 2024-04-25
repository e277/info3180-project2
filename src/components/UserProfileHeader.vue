<script setup>

import { computed, ref, watchEffect } from "vue";
import { Users, MapPin } from 'lucide-vue-next';

const props = defineProps([
  "id",
  "firstname",
  "lastname",
  "location",
  "joinedOn",
  "profilePic",
  "bio",
  "totalPosts",
  "followersCount",
  "isFollowing"
]);


let followersCount = ref(props.followersCount);
let isFollowing = ref(props.isFollowing);




let date = computed(() => {

  let dateObj = new Date(props.joinedOn);
  const month = dateObj.toLocaleString('default', { month: 'long' });
  const year = dateObj.getFullYear();

  return [month, year]
})

const token = localStorage.getItem('jwt_token');

function followUser() {
  fetch(`/api/users/${props.id}/follow`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      headers: {
        'Authorization': `Bearer ${token}`
      }
    },
    
  })
    .then(response => response.json())
    .then(data => {

      if(data.message){
        followersCount.value = data.follower_count;
        isFollowing.value = true;
      }else{
        followersCount.value = data.follower_count;
        isFollowing.value = false;
      }
      
    })
    .catch(error => {
      console.error(error);
    });
}

watchEffect(() => {
  followersCount.value = props.followersCount;
  isFollowing.value = props.isFollowing;
});

</script>


<template>
  <div class="userProfileCtn">


    <div class="picAndInfo">
      <div class="thumbnail">
        <img :src="profilePic" />
      </div>
    
      <div class="info">

        <h2>{{firstname}} {{lastname}}</h2>

        <div class="location">
          <MapPin />
          {{location}}
        </div>

        <p>{{bio}}</p>

        <p>Member since {{date[0]}} {{date[1]}}</p>



      </div>

    </div>

    <div class="metricFollowCtn">

      <div class="metrics">

        <div>

          <h3 class="count">{{totalPosts}}</h3>
          <h3>{{ totalPosts === 1 ? 'Post' : 'Posts' }}</h3>

        </div>

        <div>

          <h3 class="count" >{{followersCount}}</h3>
          <h3>{{followersCount === 1 ? 'Follower' : 'Followers' }}</h3>

        </div>
      </div>

      <div v-if="props.isFollowing != 'same user'">

        <button v-if="isFollowing == true" @click="followUser">
          <Users fill="currentColor" /> Following
        </button>

        <button v-else class="followBtn" @click="followUser">
          <Users fill="currentColor" /> Follow
        </button>
      </div>

    </div>


  </div>
</template>


<style>

.userProfileCtn{

  background-color: #ffffff;
  border-radius: 5px;
  border: 1px solid rgb(215, 215, 215);
  word-wrap: break-word;
  margin-bottom: 4rem;
  display: flex;
  padding: 3rem 5rem;
  justify-content: space-between;

}

.userProfileCtn p{
  margin: 0;
}

.userProfileCtn button{
  max-width: 200px;
  border: none;
  background-color:rgb(48, 225, 11);
}

.userProfileCtn button:hover{ 

  background-color:rgb(45, 188, 16);
}



.location{
  display: flex;
  gap: 4px;
  color: #a4a5a4;
}

.picAndInfo{
  display: flex;
  gap: 40px;
}

.info{
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  max-width: 610px;
}

.info > h2{

  font-size: 2.7rem;
  font-weight: 800;
  margin-bottom: 30px;
}

.metrics{
  display: flex;
  justify-content: space-between;
  gap: 75px;
}



.metrics > div{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  
}

.metrics h3{
  font-weight: 500;
  color: #a4a5a4;
  margin: 0;
  padding: 0;
  font-size: 1.1rem;
}

.metrics .count{
  color: #4f4e4e;
  font-weight: 900;
  font-size: 1.3rem;
}

.metricFollowCtn{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-content: center;
}

.joined{
  font-size: 0.8rem;
  color: #4f4e4e;
}

.picAndInfo .thumbnail {
  width: 180px;
  height: 180px;
  overflow: hidden;
  border-radius: 9999px;
  font-size: 0.6rem;

}

.picAndInfo .thumbnail img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;

}

</style>