<script setup>

import { ref } from "vue";
import { Heart } from 'lucide-vue-next';

defineProps([
  "profilePic",
  "username",
  "photo",
  "caption",
  "date",
  "likes",
  "current"
]);

</script>

<template>
    <div class="feedBg">

      <div class="feedPost">

          <div class="post_header">
            <div class="thumbnail">
              <img :src="profilePic" :alt="`Profile picture for ${username}`"/>
            </div>
            
            <p>{{username}}</p>
          </div>

      </div>

        <div class="post_photo">
          <img :src="photo" />
        </div>

      <div class="feedPost">
          <p class="caption">{{caption}}</p>
          
          <div class="post_footer">
            

            <div class="like_ctn">
              <Heart class="like_icon"/>
              
              <p> {{likes}} Likes</p>
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
  max-width: 700px;
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
  color: #747474;
}

.post_header{
  display: flex;
  gap: 1rem;
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  align-items: center;
}
  
.thumbnail {
  width: 60px;
  height: 60px;
  overflow: hidden;
  border-radius: 9999px;
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


</style>