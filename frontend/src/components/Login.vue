<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="Username" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    async login() {
      try {
        await axios.post('http://localhost:5000/login', {
          username: this.username,
          password: this.password
        });
        alert('Login successful!');
      } catch (error) {
        alert('Invalid credentials!');
      }
    }
  }
};
</script>
