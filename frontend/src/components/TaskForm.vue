<template>
    <div>
      <h2>{{ isEditing ? "Edit Task" : "Add New Task" }}</h2>
      <form @submit.prevent="handleSubmit">
        <label>
          Title:
          <input v-model="task.title" required />
        </label>
        <label>
          Description:
          <textarea v-model="task.description" required></textarea>
        </label>
        <label>
          Due Date:
          <input type="date" v-model="task.due_date" required />
        </label>
        <button type="submit">{{ isEditing ? "Update Task" : "Create Task" }}</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: {
      taskToEdit: {
        type: Object,
        default: null,
      },
    },
    data() {
      return {
        task: {
          title: "",
          description: "",
          due_date: "",
        },
        isEditing: false,
      };
    },
    methods: {
      async handleSubmit() {
        try {
          if (this.isEditing) {
            await axios.put(`http://127.0.0.1:5000/tasks/${this.taskToEdit.id}`, this.task);
          } else {
            await axios.post("http://127.0.0.1:5000/tasks", this.task);
          }
          this.$emit("taskUpdated");
        } catch (error) {
          console.error("Error submitting task:", error);
        }
      },
    },
    watch: {
      taskToEdit: {
        handler(newValue) {
          if (newValue) {
            this.task = { ...newValue };
            this.isEditing = true;
          } else {
            this.task = { title: "", description: "", due_date: "" };
            this.isEditing = false;
          }
        },
        immediate: true,
      },
    },
  };
  </script>
  