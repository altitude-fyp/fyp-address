<template>
  <v-container>
    <v-file-input @change="onInput"/>

    <div>
        <pre>
          {{ data }}
        </pre>
    </div>
  </v-container>
</template>

<script>
import Papa from "papaparse"

export default {
  data() {
    return {
      data: null //return nothing when initialise
    }
  },
  methods: {
    onInput(file) {
      Papa.parse(file, {
        complete: (results) => {
          this.data = results.data
        }
      })
    }
  }
}
</script>
