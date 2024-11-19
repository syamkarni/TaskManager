<template>
    <div>
      <form @submit.prevent="handleSubmit">
        <div>
          <label for="title">Title:</label>
          <input id="title" v-model="task.title" placeholder="Enter task title" required />
        </div>
        <div>
          <label for="description">Description:</label>
          <textarea
            id="description"
            v-model="task.description"
            placeholder="Enter task description"
            required
          ></textarea>
        </div>
        <div>
          <label for="due_date">Due Date:</label>
          <input id="due_date" type="date" v-model="task.due_date" required />
        </div>
        <button type="submit">Create Task</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        task: {
          title: "",
          description: "",
          due_date: "",
        },
      };
    },
    methods: {
      async handleSubmit() {
        try {

            await axios.post("http://127.0.0.1:5000/tasks", this.task, {
                headers: {
                    Authorization: "Bearer mysecrettoken",
                },
                });
  

          this.$emit("taskUpdated");
  

          this.task = {
            title: "",
            description: "",
            due_date: "",
          };
        } catch (error) {
          console.error("Error creating task:", error);
        }
      },
    },
  };
  </script>
  