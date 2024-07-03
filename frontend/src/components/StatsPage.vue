<template>
    <div>
        <h2>OSoMe Stats</h2>
        {{ user }}
    </div>
    <div v-if="user.isLoggedIn.value">
        {{ data }}
    </div>
    <div v-else>
        Please log in to view stats
    </div>
</template>
  
<script lang="ts">
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useUser } from '../composables/useUser'
import { useRouter } from 'vue-router';

export default {
    setup() {
        const apiBaseUrl = import.meta.env.VITE_APP_API_BASE_URL;
        const user = useUser();
        const data = ref(null);
        const router = useRouter();

        const getAllData = async () => {
            try {
                const response = await axios.get(`${apiBaseUrl}/api/stats/`);
                console.log("response", response)
                data.value = response.data
            } catch (error) {
                console.error(`Error: ${error}`);
            }
        };

        onMounted(() => {
            if (user.isLoggedIn.value) {
                getAllData();
            } else {
                router.push('/');
            }
        });

        return {
            apiBaseUrl,
            user,
            data,
            getAllData
        };
    }
};
</script>
  