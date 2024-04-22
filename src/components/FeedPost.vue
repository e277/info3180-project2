<script setup>

import { ref } from "vue";
import { Heart } from 'lucide-vue-next';

defineProps([
  "profilePic",
  "username",
  "photo",
  "caption",
  "likes",
  "date"
]);

</script>

<template>
    <div>

        <p>
        {{profilePic}}
        {{username}}
        {{photo}}
        {{caption}}
        {{likes}}
        {{date}}
        </p>
    </div>

    <Heart />

</template>

<style>


  
</style>