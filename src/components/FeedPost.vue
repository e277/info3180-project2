<script setup>

import { ref } from "vue";
import { Heart } from 'lucide-vue-next';

defineProps([
  "profilePic",
  "userId",
  "username",
  "photo",
  "caption",
  "date",
  "likes",
  "isLiked"
  
]);

</script>

<template>
    <div class="feedBg">

      <div class="feedPost">

          <div class="post_header">
            <a class="profileLink" :href="'/profile/' + userId"> 
              <div class="thumbnail">
                <img :src="profilePic" :alt="`Profile picture for ${username}`"/>
              </div>
            
            
              <p>{{username}}</p>

            </a>
          </div>

      </div>

        <div class="post_photo">
          <img :src="photo" />
        </div>

      <div class="feedPost">
          <p class="caption">{{caption}} Creating memories by the seaside. Waves of laughter. Enjoying the tranquility of the ocean breeze and the warmth of the sun.</p>
          
          <div class="post_footer">
            

            <div class="like_ctn">
              <Heart v-if="isLiked == false" color="#747474" class="like_icon"/>
              <Heart v-else color="#ee3543" fill="#ee3543" class="like_icon"/>
              
              
              <p> {{likes}} {{ likes === 1 ? 'Like' : 'Likes' }}</p>
            </div>

            <p>{{date}}</p>
          </div>

      </div>
    </div>

</template>

<style>

.feedBg{
  background-color: #ffffff;
  border-radius: 5px;
  border: 1px solid rgb(215, 215, 215);
  width: 100%;
  max-width: 600px;
  word-wrap: break-word;
  margin-bottom: 4rem;

}

.feedPost{
  display: flex;
  flex-direction: column;
  padding: 1rem;
}

.post_footer{
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 2px;
  font-size: 0.8rem;
  font-weight: 500;
  color: #a4a5a4;
}

.post_footer > p{
  margin: 0;
}

.like_ctn{
  display: flex;
  align-items: baseline;

}

.like_icon{
  align-self: flex-start;
  margin-right: 4px;
}


.thumbnail {
  width: 50px;
  height: 50px;
  overflow: hidden;
  border-radius: 9999px;
  font-size: 0.6rem;

}

.thumbnail img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;

}

.post_photo {
  width: 100%;
  height: 350px;
  overflow: hidden;
}

.post_photo img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;

}

.profileLink{

  all: unset;
  display: flex;
  max-width: fit-content;
  gap: 1rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  align-items: center;
  cursor: pointer;
}

.profileLink:hover{
  color: rgb(32, 168, 173);
}


</style>