<template>
  <div>
    <h2>Workouts</h2>
    <input v-model="searchQuery" placeholder="Search workouts" />
    <ul>
      <li v-for="workout in filteredWorkouts" :key="workout.id">{{ workout.name }} ({{ workout.level }})</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      workouts: [],
      searchQuery: ''
    };
  },
  computed: {
    filteredWorkouts() {
      return this.workouts.filter(workout =>
        workout.name.toLowerCase().includes(this.searchQuery.toLowerCase())
      );
    }
  },
  async created() {
    const response = await axios.get('http://localhost:5000/workouts');
    this.workouts = response.data;
  }
};
</script>
