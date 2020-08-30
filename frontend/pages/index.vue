<template>
  <!--This is the main page where it is just '/'-->
  <v-app>
    <c-s-v-search/>
    <google-map/>

  </v-app>
</template>

<script>

import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";

export default {
  components: {
    CSVSearch,
    GoogleMap,
  }
}
</script>
