<template>
    <div>
        <div class="rvt-layout__wrapper [ rvt-p-tb-xl ]">
            <div class="rvt-container-lg">
                <div class="rvt-row">
                    <div class="rvt-cols-4-md rvt-flow rvt-prose">
                        <form @submit.prevent="handleSubmit">
                            <fieldset class="rvt-fieldset">
                                <legend class="rvt-legend [ rvt-ts-18 rvt-border-bottom rvt-p-bottom-xs ]">Login</legend>
                                <p class="rvt-ts-14">Required fields are marked with <span class="rvt-color-orange-500 rvt-text-bold">*</span></p>
                                <div class="rvt-m-top-sm">
                                    <label class="rvt-label" for="username">Username <span class="rvt-color-orange-500 rvt-text-bold">*</span></label>
                                    <input class="rvt-input" type="text" id="username" autocomplete="username" v-model="username" required>
                                </div>
                                <div class="rvt-m-top-sm">
                                    <label class="rvt-label" for="password">Password <span class="rvt-color-orange-500 rvt-text-bold">*</span></label>
                                    <input class="rvt-input" type="password" id="password" autocomplete="current-password" v-model="password" required>
                                </div>
                                <div class="rvt-m-top-lg">
                                </div>
                            </fieldset>
                            <button type="submit" class="rvt-button">Login</button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
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
  