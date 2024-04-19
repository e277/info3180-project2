<template>
<div>
<h1>New Post</h1>
<post-form></post-form>
</div>
</template>

<script setup>
import { defineComponent } from 'vue';
import PostForm from '@/components/NewPostForm.vue';

defineComponent({
components:{
    PostForm,
},
});
</script>

<style scoped>
h1{
    margin-left:400px;
    padding-top:30px;
}
</style>