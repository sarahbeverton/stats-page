<template>
    <div>
        <LoginPage v-if="!isLoggedIn" @login="handleLogin" />
        <StatsPage v-else />
    </div>
</template>
  
<script lang="ts" setup>
import { ref } from 'vue';
import { useUser } from '../composables/useUser';
import LoginPage from './LoginPage.vue';
import StatsPage from './StatsPage.vue';

const user = useUser();
const isLoggedIn = ref(user.isLoggedIn);

const handleLogin = () => {
    isLoggedIn.value = true;
};
</script>
