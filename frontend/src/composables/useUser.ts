import { reactive, computed } from 'vue';

interface UserState {
  isLoggedIn: boolean;
}

const state = reactive<UserState>({
  isLoggedIn: false,
});

export function useUser() {
  const isLoggedIn = computed(() => state.isLoggedIn);

  function login() {
    state.isLoggedIn = true;
  }

  function logout() {
    state.isLoggedIn = false;
  }

  return {
    isLoggedIn,
    login,
    logout,
  };
}
