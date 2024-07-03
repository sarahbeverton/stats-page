<template>
    <div>
        <h2>Login</h2>
        <form @submit.prevent="handleSubmit">
            <div>
                <label for="username">Username:</label>
                <input id="username" v-model="username" type="text" autocomplete="username" required>
            </div>
            <div>
                <label for="password">Password:</label>
                <input id="password" v-model="password" type="password" autocomplete="current-password" required>
            </div>
            <button type="submit">Login</button>
            <div>{{  user }}</div>
        </form>
    </div>
</template>
  
<script lang="ts">
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useUser } from '../composables/useUser'


export default {
    setup() {
        const username = ref('');
        const password = ref('');
        const apiBaseUrl = import.meta.env.VITE_APP_API_BASE_URL;
        const router = useRouter();
        const user = useUser();

        const handleSubmit = async () => {
            try {
                const response = await axios.post(`${apiBaseUrl}/api/login/`, {
                    username: username.value,
                    password: password.value
                });

                if (response.status === 200) {
                    user.login();
                    await router.push('/stats');
                    console.log('Login successful');
                } else {
                    console.log('Error logging in');
                }
            } catch (error) {
                console.error(`Error: ${error}`);
            }
        };

        return {
            username,
            password,
            apiBaseUrl,
            user,
            handleSubmit
        };
    }
};
</script>
  