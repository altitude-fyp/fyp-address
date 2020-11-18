<template>
  <div>

    {{selectedRegions}}

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

    <div v-if="selectedRegions && regionPolygons && regionPolygonsMap">
      <div v-for="(region,i) in selectedRegions" :key=i>
                    <GmapPolygon
                        :paths="regionPolygonsMap[region.toLowerCase()]"
                        :options="{
                            strokeColor: '#FF0000',
                            strokeOpacity: 1,
                            strokeWeight: 2,
                            fillColor: '#FF0000',
                            fillOpacity: 0.4
                        }"

                        />
      </div>
    </div>



    </GmapMap>
  </div>
</template>

<script>
export default {
  name: "GoogleMapAnalytics",
  props: ["coordinates", "selectedRegions"],
  data() {
    return {
      //lat and lng returns singapore by default
      center: {lat: 1.3521, lng: 103.8198},
      markers: [],
      regionPolygons: null,
      regionPolygonsMap: null,
    };
  },
  mounted() {
    this.getRegionPolygons()
  },

  methods: {

    getRegionPolygons() {
      let url = process.env.BACKEND + "/api/regions/polygons"

      this.$axios.get(url).then((response) => {
          this.regionPolygons = response.data
          
          let map = {}
          for (let i=0; i<this.regionPolygons.length; i++) {
              map[this.regionPolygons[i]["_id"]] = this.regionPolygons[i]["polygon"]
          }
          this.regionPolygonsMap = map

          console.log(this.regionPolygonsMap)

      })
    },


  },
};
</script>
<style scoped>
</style>