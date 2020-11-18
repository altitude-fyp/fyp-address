<template>
  <div>
    <GmapMap
      :options="{
         zoomControl: true,
         mapTypeControl: false,
         scaleControl: false,
         streetViewControl: false,
         rotateControl: false,
         fullscreenControl: false,
         disableDefaultUi: false
       }"
      :center="center"
      :zoom="11"
      style="
        width:40%;
        position:fixed;
        right:0px;
        height:100%;
        overflow:hidden;"
      >
    </GmapMap>
  </div>
</template>

<script>
export default {
  name: "GoogleMapAnalytics",
  props: {
    coordinates: {
      type: Array,
    },
  },
  data() {
    return {
      //lat and lng returns singapore by default
      center: {lat: 1.3521, lng: 103.8198},
      markers: [],
    };
  },
  mounted() {

  },

  methods: {


  },
};
</script>
<style scoped>
</style>