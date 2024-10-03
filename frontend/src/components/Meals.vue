<template>
  <div>
    <h2>Meals</h2>
    <ul>
      <li v-for="meal in meals" :key="meal.id">{{ meal.name }} ({{ meal.type }})</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      meals: []
    };
  },
  async created() {
    const response = await axios.get('http://localhost:5000/meals');
    this.meals = response.data;
  }
};
</script>
