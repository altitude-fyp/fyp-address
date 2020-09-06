<template>
  <!--This is the main page where it is just '/'-->
  <v-app>
    <google-map/>
    <v-container>
      <google-bottom-sheet/>
    </v-container>
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
