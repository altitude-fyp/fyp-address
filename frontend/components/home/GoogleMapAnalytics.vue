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
    this.geolocate();
  },

  methods: {
    addMarker(event) {
      console.log(this.coordinates)
      const marker = {
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      };
      this.markers.push({position: marker});
    },

    geolocate: function () {
      navigator.geolocation.getCurrentPosition(position => {
        this.center = {
          lat: position.coords.latitude,
          lng: position.coords.longitude
        };
      });
    },

  },
};
</script>
<style scoped>
</style>