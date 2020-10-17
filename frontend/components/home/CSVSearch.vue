<template>
  <!--fluid style="padding-top: 400px; padding-left: 240px; position:absolute; z-index: 1;"-->
  <v-container >
    <v-row>
      <v-col cols="2" style="padding-top: 20px;">
        <v-select
          v-model="preselect"
          :items="items"
          menu-props="auto"
          label="Country"
          hide-details
          prepend-icon="mdi-map"
          outlined
          dense
        ></v-select>
      </v-col>
      <v-col cols="10">
        <v-text-field
          v-model="address"
          prepend-inner-icon="mdi-magnify"
          placeholder="Enter an address, hit 'Enter' to search"
          v-on:keypress.enter="lookUpAddress"
        >
        </v-text-field>
      </v-col>
    </v-row>


  </v-container>

</template>

<script>
export default {
  name: "CSVSearch",
  data() {
    return{
      preselect: 'Singapore',
      address: '',
      items: ['Singapore', 'USA'],
    }
  },
  methods: {
    lookUpAddress(){
      /*console.log(this.preselect)
      console.log(this.address)*/
    }

  }

}
</script>

<style scoped>

</style>

