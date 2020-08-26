<template>
  <div>
    <div v-for="anythingElse in lists" class="card">
      <n-link :to="`/admin/users/${anythingElse.id}`">
        <v-card>
          <cool-todo :id="anythingElse.id" :title="anythingElse.title"></cool-todo>
        </v-card>
      </n-link>
    </div>
  </div>
</template>

<script>
import CoolTodo from "~/components/CoolTodo";

export default {
  components: {CoolTodo},
  asyncData({$axios}) {
    return $axios.$get('https://jsonplaceholder.typicode.com/todos')
      .then((data) => {
        return {
          lists: data
        }
      })
  },
}
</script>

<style scoped lang="scss">
.card {
  padding-bottom: 24px;
}
</style>
