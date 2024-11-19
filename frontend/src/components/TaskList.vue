<template>
    <div>
      <h1>Task List</h1>
      <div v-for="task in tasks" :key="task.id" class="task-card">
        <h3>{{ task.title }}</h3>
        <p>{{ task.description }}</p>
        <p>Due: {{ task.due_date }}</p>
        <p>Status: {{ task.status }}</p>
        <button @click="markComplete(task.id)">Mark Complete</button>
        <button @click="deleteTask(task.id)">Delete</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        tasks: [],
      };
    },
    methods: {
      async fetchTasks() {
        try {
          const response = await axios.get("http://127.0.0.1:5000/tasks");
          this.tasks = response.data;
        } catch (error) {
          console.error("Error fetching tasks:", error);
        }
      },
      async markComplete(id) {
        try {
          await axios.patch(`http://127.0.0.1:5000/tasks/${id}/complete`);
          this.fetchTasks();
        } catch (error) {
          console.error("Error marking task complete:", error);
        }
      },
      async deleteTask(id) {
        try {
          await axios.delete(`http://127.0.0.1:5000/tasks/${id}`);
          this.fetchTasks();
        } catch (error) {
          console.error("Error deleting task:", error);
        }
      },
    },
    mounted() {
      this.fetchTasks();
    },
  };
  </script>
  
  <style>
  .task-card {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 10px;
    border-radius: 5px;
  }
  </style>
  