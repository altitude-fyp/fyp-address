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
      <div>
        <GmapPolygon
          v-for="region in regionPolygons"
          :key=region.country
          :paths="region.polygon"
          :options="polygonOptions" />

      </div>

      <!-- infowindow test -->
      <GmapInfoWindow 
        :options="{
          content: 'this is an infowindow'
        }"
        :position=center />


      <!-- marker clustering test goes here -->
      <GmapCluster>
        <GmapMarker 
          v-for="position in testMarkers"
          :key="position.lat + Math.random()"
          :position=position
          />

      </GmapCluster>

    </GmapMap>

  </div>
</template>

<script>

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
    this.temp()
  },


  methods: {

    temp() {
      //this function is temporary and is to be integrated with region functions

      let url = process.env.BACKEND + "/api/regions/polygons/paya lebar,changi,yishun,bishan,aljunied,newton,boon lay,jurong east"

      this.$axios.get(url).then((response) => {
        this.regionPolygons = response.data
      })

      url = process.env.BACKEND + "/api/regions/polygons/serangoon"
      this.$axios.get(url).then((response) => {
        this.testMarkers = response.data[0].polygon
      })

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

