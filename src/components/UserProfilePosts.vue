<script setup>

import { ref } from "vue";
import { Heart } from 'lucide-vue-next';

defineProps([
  "id",
  "photo", 
]);

</script>


<template>

  <div class="postthumbnail">
    <img :src="photo" />
  </div>

</template>

<style>

.postthumbnail {
  width: 430px;
  height: 430px;
  overflow: hidden;

}

.postthumbnail img{
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;

}

</style>