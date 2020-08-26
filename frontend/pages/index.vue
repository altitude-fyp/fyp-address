<template>
  <!--This is the main page-->
  <google-map/>


</template>

<script>
import Logo from '~/components/Logo.vue'
import VuetifyLogo from '~/components/VuetifyLogo.vue'
import GoogleMap from "@/components/GoogleMap";

export default {
  components: {
    GoogleMap,
    Logo,
    VuetifyLogo
  }
}
</script>
