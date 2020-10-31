<template>
    <!-- Search Country -->
      <v-row justify="center">
          <v-col cols="11">
          <v-autocomplete class="elevation-0"
            v-model="selectedCountry"
            :items="allCountries"
            rounded
            solo
            label="Enter country name"
          ></v-autocomplete>
          </v-col>

        <v-col cols="1">
        <div style="margin-top:5px">
        <v-btn
          depressed
          color="primary"
          @click="submitSelectedCountry"
        >
          Search
        </v-btn>
        </div>
        </v-col>
      </v-row>

</template>

<script>

export default {
    
    name: "npl-country-selection",

    data() {
        return {
            allCountries: null,
            selectedCountry: []
        }
    },

    mounted() {
        this.getAllCountries()
    },

    methods: {

        getAllCountries() {
            //this function gets all countries from backend in alphabetical order
            var url = process.env.BACKEND + "/api/countries/list"

            this.$axios.get(url).then((response) => {
                this.allCountries = response.data.countries
            })  
        },

        submitSelectedCountry() {
            //this function is called when user clicks "submit" button
            //this function passes selectedCountries to the parent component
            this.$emit("submitSelectedCountriesEvent", this.selectedCountry)
        }
    },

}
</script>

<style>
</style>