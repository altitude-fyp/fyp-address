<template>
  <v-container>

<!--    CODE INSIDE HERE-->
    <li v-for="item in items" :key="item.name">
      {{ item.name }}
      {{ item.type }}
      <v-icon>{{ item.icon }}</v-icon>
    </li>
  </v-container>
</template>

<script>
export default {
  name: "scheduledJob",
  data() {
    return {
      items: [
        {name: 'Singapore Cust', type: "Customers", freq: 'Monthly',icon: 'mdi-bell'},
        {name: 'Singapore Cust', type: "Customers", freq: 'Monthly',icon: 'mdi-bell'},
        {name: 'Singapore Cust', type: "Customers", freq: 'Monthly',icon: 'mdi-bell'}
      ]
      };
    }
}
</script>

<!-- CSS-->
<style scoped>

</style>
