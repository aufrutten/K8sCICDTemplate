<script setup lang="ts">
import { onMounted, ref } from "vue";
import { accountData } from "@/stores/account";
import type { AxiosError, AxiosResponse } from "axios";

const account = accountData()
const errors: any = ref(false)

onMounted(() => {
  // Check if the URL contains an access token
  const urlParams = new URLSearchParams(window.location.hash.substring(1));
  if (urlParams.has('access_token')) {
    sendAccessTokenToBackend(urlParams.get('access_token') || '');
  }
});

const sendAccessTokenToBackend = (token: string) => {
  window.api.put("/accounts/auth/google-oauth2", {provider_token: token})
    .then((response: AxiosResponse) => {
        account.connect_account(response.data.email, response.data.access_token, response.data.refresh_token)
        account.router.replace({name: 'home'})
    })
    .catch((error: AxiosError) => {
        errors.value = error.response?.data
    });
};
</script>

<template>
    <h1 class="align-middle d-flex justify-content-center">callback google</h1>
    <br>
    <div v-if="errors">
      <ul class="list-group list-group-flush">
        <li class="list-group-item" style="font-size: 24px">Try another account...</li>
        <li class="list-group-item" style="font-size: 24px">Errors</li>
        <li class="list-group-item" v-for="error in errors">{{error}}</li>
      </ul>
    </div>
</template>

<style scoped>
h1 {
  margin-top: 20%;
}
.list-group {
  margin-right: 35%;
  margin-left: 35%;
  text-align: center;
}

li {
  text-align: center;
}
</style>