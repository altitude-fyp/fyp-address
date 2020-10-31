<template>
  
  <div v-if="coordinates">

    <!-- Google map component starts here -->
    <GmapMap
      :options=gmapOptions
      :center=center
      :zoom="zoom"
      style="min-width: 100%; min-height: 500px;">

      <!-- google map marker goes here -->
      <div v-if="coordinates">
        
        <GmapMarker
          v-for="country in coordinates"
          :position="{lat: country.lat, lng: country.lon}"
          :key="country.name"/>

      </div>

      <!-- temp: polygon goes here -->
      <div v-for="[i,region] in Object.entries(regionPolygons)" :key=i>

        <GmapPolygon
          :paths="region.polygon"
          :options="polygonOptions"
          @click="toggleShowInfoWindow(i)" />
      
        <GmapInfoWindow 
          v-if="region.showInfoWindow"
          :key=region.name
          :options="{content: getGmapInfoWindowContent(region)}"
          :position=region.center />
        
      </div>

      <!-- marker clustering test goes here -->
      <!-- <GmapCluster>
        <GmapMarker 
          v-for="position in testMarkers"
          :key="position.lat + Math.random()"
          :position=position />
      </GmapCluster> -->

    </GmapMap>

  </div>

</template>

<script>
import func from '../../vue-temp/vue-editor-bridge';

export default {

  name: "GoogleMap",
  
  props: ["coordinates"],
  
  data() {
    return {

      gmapOptions: {
        zoomControl: true,
        mapTypeControl: false,
        scaleControl: false,
        streetViewControl: false,
        rotateControl: false,
        fullscreenControl: false,
        disableDefaultUi: false
      },

      polygonOptions: {
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
      },

      regionPolygons: [],
    
      testMarkers: null

    };
  },


  mounted() {
    this.pullRegionPolygonData()
  },


  methods: {

    pullRegionPolygonData() {
      //this function gets polygon data from Singapore for all regions (with valid data)

      let url = process.env.BACKEND + "/api/regions/polygons"

      this.$axios.get(url).then((response) => {
        this.regionPolygons = response.data
      })

    },

    toggleShowInfoWindow(i) {
      this.regionPolygons[i].showInfoWindow = !this.regionPolygons[i].showInfoWindow
    },

    getGmapInfoWindowContent(region) {
      // let income = region.data["Income From Work"]
      // let incomeOver6k = 100
      
      // return `
      //   <v-container>
      //     <strong>${region.name.slice(0,1).toUpperCase() + region.name.slice(1)}</strong><br>
      //     Income over 6k: <br>


      //   </v-container>`
      return "hello"
    },

  },


  computed: {

    center() {
      let lat = 0
      let lng = 0

      for (let i in this.coordinates) {
        let coordinate = this.coordinates[i]
        lat += coordinate.lat
        lng += coordinate.lon
      }

      return {lat:lat/this.coordinates.length, lng:lng/this.coordinates.length}

    },

    zoom() {
      if (this.coordinates.length==1 && this.coordinates[0].country == "Singapore") return 12
      if (this.coordinates.length == 1) return 6
      return 3
    }


  }
};
</script>

