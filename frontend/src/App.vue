<template>
  <div id="app">
    <header>
      <h1>Task Manager</h1>
    </header>
    <main>
      <section class="task-form">
        <TaskForm @taskUpdated="refreshTasks" />
      </section>
      <section class="task-list">
        <TaskList :refreshKey="refreshKey" />
      </section>
    </main>
  </div>
</template>

<script>
import TaskForm from './components/TaskForm.vue';
import TaskList from './components/TaskList.vue';

export default {
  name: 'App',
  components: {
    TaskForm,
    TaskList,
  },
  data() {
    return {
      refreshKey: 0,
    };
  },
  methods: {
    refreshTasks() {
      this.refreshKey += 1;
    },
  },
};
</script>


<style>

#app {
  font-family: "Arial", sans-serif;
  text-align: center;
  color: #333;
  margin: 0;
  padding: 0;
  background-color: #f8f9fa;
  min-height: 100vh;
}

header {
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
  padding: 20px;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
}

header h1 {
  margin: 0;
  font-size: 28px;
  color: #333;
}


main {
  max-width: 800px;
  margin: 40px auto;
  padding: 20px;
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}


.task-form {
  margin-bottom: 30px;
}

.task-form h2 {
  font-size: 20px;
  margin-bottom: 20px;
}


.task-list h2 {
  font-size: 20px;
  margin-bottom: 20px;
}

.task-list .task-card {
  text-align: left;
  background: #f9f9f9;
  border: 1px solid #e0e0e0;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}


button {
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 4px;
  font-size: 14px;
  cursor: pointer;
}

button:hover {
  opacity: 0.9;
}

button:first-of-type {
  background-color: #4caf50;
  color: white;
}

button:last-of-type {
  background-color: #f44336;
  color: white;
}


input,
textarea {
  width: calc(100% - 20px);
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 14px;
  box-sizing: border-box;
}

input:focus,
textarea:focus {
  outline: none;
  border-color: #4caf50;
  box-shadow: 0 0 5px rgba(76, 175, 80, 0.5);
}
</style>
