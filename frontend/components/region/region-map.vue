<template>
    <div>

        <GmapMap
            :options=gmapOptions
            :center=center
            :zoom="11.8"
            style="min-width:100%; min-height: 600px;">

            <!-- temp: polygon goes here -->
            <div v-for="[i,region] in Object.entries(regionPolygons)" :key=i>

                <GmapPolygon
                :paths="region.polygon"
                :options="getPolygonOptions(region)"
                @click="setInfoWindowRegion(i)" />
                
            </div>

            <GmapInfoWindow 
                v-if="infoWindowRegion"
                :position=infoWindowRegion.center
                @closeclick="infoWindowRegion=null"> 

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

    props: ["selectedRegions"],

    data() {
        return {

            center: {lat:1.3521, lng:103.8198},

            gmapOptions: {
                zoomControl: true,
                mapTypeControl: false,
                scaleControl: false,
                streetViewControl: false,
                rotateControl: false,
                fullscreenControl: false,
                disableDefaultUi: false
            },

            regionPolygons: [],
            infoWindowRegion: null,

        }
    },

    mounted() {
        let url = process.env.BACKEND + "/api/regions/polygons"

        this.$axios.get(url).then((response) => {
            this.regionPolygons = response.data
        })
    },

    methods: {

        setInfoWindowRegion(i) {
            this.infoWindowRegion = this.regionPolygons[i]
        },

        goToRegion() {
            this.$emit("regionSelectedOnMap", [this.infoWindowRegion.name])
        },


        getPolygonOptions(region) {

            let color = "#0000CC"

            if (region.undocumented) color = "#000000"

            if (this.selectedRegions.includes(region.name)) {
                color = "#FF0000"
            }

            return {
                strokeColor: color,
                strokeOpacity: 1,
                strokeWeight: 2,
                fillColor: color,
                fillOpacity: 0.35,
            }
        },

    },

    computed: {

        infoWindowRegionName() {
            return this.infoWindowRegion.name.slice(0,1).toUpperCase() + this.infoWindowRegion.name.slice(1)
        },


        infoWindowRegionBody() {
            
            try {
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

            catch {
                return `
                    Data not available!
                `
            }
        },

    }



}

</script>