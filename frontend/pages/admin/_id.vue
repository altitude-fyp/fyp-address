<template>
  <div>
    <h1>
      {{ id }}
    </h1>
    <h3>
      {{ text }}
    </h3>
    <h4>
      {{ coolerText }}
    </h4>
    <button @click="method">
      Click Me
    </button>

    <n-link to="/my-people">
      My People
    </n-link>
    <div>
      <!--      {{ name }}-->
    </div>
  </div>
</template>

<script>
export default {
  asyncData({params: {id}}) {
    return {
      id
    }
  },
  data() {
    return {
      text: "",
      coolerAdder: "ADDED"
    }
  },
  methods: {
    method() {
      this.text += this.id
      this.coolerAdder += this.id
    }
  },
  computed: {
    coolerText() {
      return this.text + " " + this.coolerAdder
    }
  },
  mounted() {
    setInterval(() => {
      this.text += "Cool"
    }, 3000)
  }
}
</script>

<style scoped>

</style>
