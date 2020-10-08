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
      :zoom="2"
      style="min-width: 100%; min-height: 500px;"
    >
      <!--if you require markers, unpack this-->
      <div v-if="coordinates">
        <GmapMarker
          :key="index"
          v-for="(c, index) in coordinates"
          :position="{lat:c.lat, lng: c.long,}"
        />
      </div>

      <!-- This is to remove info window on first click-->
      <gmap-info-window :opened="false"/>

    </GmapMap>
  </div>
</template>

<script>
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet";
import CSVSearch from "@/components/home/CSVSearch";

export default {
  name: "GoogleMap",
  components: {CSVSearch, GoogleBottomSheet},
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
