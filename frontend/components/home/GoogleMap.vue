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
          @click="setInfoWindowRegion(i)" />
        
      </div>

      <GmapInfoWindow 
        v-if="infoWindowRegion"
        :position=infoWindowRegion.center> 

          <v-container align="center" justify="center">

            <span class="font-weight-medium">
              {{infoWindowRegionName}}
            </span>

            <br>

            <div v-html="infoWindowRegionBody"/>

            <br>

            <v-btn block @click="goToRegion">
              Go to {{infoWindowRegionName}}
            </v-btn>

          </v-container>

      </GmapInfoWindow>

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
      infoWindowRegion: null,

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

    setInfoWindowRegion(i) {
      this.infoWindowRegion = this.regionPolygons[i]
    },


    goToRegion() {
      // to be completed
    }

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
    },


    infoWindowRegionName() {
      return this.infoWindowRegion.name.slice(0,1).toUpperCase() + this.infoWindowRegion.name.slice(1)
    },


    infoWindowRegionBody() {
      let region = this.infoWindowRegion

      let income = region.data["Income From Work"]
      let incomeOver6k = "" + Math.round(income["6000+"] / Object.values(income).reduce((total,n) => total+n) * 100) + "%"
      
      let house = region.data["Type Of Dwelling Household"]
      let hdb = Math.round( house["hdb"] / Object.values(house).reduce((total,n) => total+n ) * 100) + "%"

      return `
        Income over 6k: ${incomeOver6k} <br>
        Proportion living in HDB: ${hdb} <br>
      `
    }


  }
};
</script>

