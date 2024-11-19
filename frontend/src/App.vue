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

