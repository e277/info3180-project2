<script setup>

import { ref } from "vue";
import { Heart } from 'lucide-vue-next';

defineProps([
  "id",
  "user_id",
  "photo",
  "totalPosts",
  "firstname",
  "lastname",
  "location",
  "joinedOn",
  "profilePic",
  "followersCount" 
]);

</script>