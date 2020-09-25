<template>
  <!--This is the main page where it is just '/'-->
  <v-app>
    <google-map/>
    <c-s-v-search/>
    <GoogleBottomSheet/>
  </v-app>
</template>

<script>

import GoogleMap from "@/components/home/GoogleMap";
import GoogleBottomSheet from "~/components/home/GoogleBottomSheet";
import CSVSearch from "@/components/home/CSVSearch";

export default {
  components: {
    CSVSearch,
    GoogleBottomSheet,
    GoogleMap,

  }
}
</script>
<style scoped>


</style>
