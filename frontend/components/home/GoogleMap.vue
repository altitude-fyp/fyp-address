<template>
  <div>
  <v-container fluid style="width: 100%; height: 60%;">
    <c-s-v-search/>
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
      :zoom="12"
      style="width: 100%; height: 100%;"
      @click="addMarker"
    >

      <!--if you require markers, unpack this-->
      <GmapMarker
        :key="index"
        v-for="(m, index) in markers"
        :position="m.position"
        :clickable="true"
        :draggable="true"
        @click="removeMarker"
      />

      <!-- This is to remove info window on first click-->
      <gmap-info-window :opened="false"/>

    </GmapMap>
  </v-container>

  </div>
</template>

<script>
import {gmapApi} from 'vue2-google-maps'
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet";
import CSVSearch from "@/components/home/CSVSearch";

export default {
  name: "GoogleMap",
  components: {CountryRegion, CSVSearch, GoogleBottomSheet},
  data() {
    return {
      //lat and lng returns singapore by default
      center: {lat: 1.3521, lng: 103.8198},
      markers: [],
      coordinates: null,
      sheet: false
    };
  },

  mounted() {
    //this.geolocate();
  },

  methods: {
    changeSheet() {
      this.sheet = false
    },
    addMarker(event) {
      this.sheet = true
      const marker = {
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      };
      this.markers.push({position: marker});
    },
    removeMarker(event) {
      this.sheet = true
      const marker = {
        lat: event.latLng.lat(),
        lng: event.latLng.lng()
      };
      for (var i = 0; i < this.markers.length; i++) {
        var accessed = this.markers[i]['position']
        if (marker.lat == accessed['lat'] && marker.lng == accessed['lng']) {
          this.markers.splice(i, 1)
        }
      }
    },
  },
  computed: {}
};
</script>
