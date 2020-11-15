<template>
    <div>

        <GmapMap
            :options=gmapOptions
            :center=center
            :zoom="11.8"
            style="min-width:100%; min-height: 600px;">


            <div v-if="!marketSegmentation">
                <!-- temp: polygon goes here -->
                <div v-for="[i,region] in Object.entries(regionPolygons)" :key=i>

                    <GmapPolygon
                        v-if="selectedRegions"
                        :paths="region.polygon"
                        :options="{
                            strokeColor: color(i),
                            strokeOpacity: 1,
                            strokeWeight: 2,
                            fillColor: color(i),
                            fillOpacity: 0.35,
                        }"
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
            </div>

            <!-- <GmapCluster>
                <GmapMarker 
                v-for="position in testMarkers"
                :key="position.lat + Math.random()"
                :position=position />
            </GmapCluster> -->


        </GmapMap>

        <div v-for="(region,i) in marketSegmentationRegions" :key=i>
            {{region}}
        </div>

    </div>
</template>

<script>

export default {

    props: ["selectedRegions", "marketSegmentation", "marketSegmentationRegions"],

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
        this.getRegionPolygons()
    },

    methods: {

        getRegionPolygons() {
            let url = process.env.BACKEND + "/api/regions/polygons"

            this.$axios.get(url).then((response) => {
                this.regionPolygons = response.data
            })
        },

        setInfoWindowRegion(i) {
            this.infoWindowRegion = this.regionPolygons[i]
        },

        goToRegion() {
            this.$emit("regionSelectedOnMap", [this.infoWindowRegion.name])
        },


        color(i) {
            let region = this.regionPolygons[i]
            if (region.undocumented) return "#000000"
            if (this.selectedRegions.includes(region.name.toLowerCase())) return "#FF0000"
            return "#0000CC"
            
        },

        sum(o) {
            // returns sums of values of object
            return Object.values(o).reduce((a,b)=>a+b)
        },

        percentage(obj, keys) {
            // returns percentage of key in object
            let out = 0
            
            for (let i=0; i<keys.length; i++) {
                out += obj[keys[i]] / this.sum(obj)
            }

            return (out * 100).toFixed(1)

        }

    },

    computed: {

        infoWindowRegionName() {
            return this.infoWindowRegion.name.slice(0,1).toUpperCase() + this.infoWindowRegion.name.slice(1)
        },


        infoWindowRegionBody() {
            
            try {
                let region = this.infoWindowRegion

                let econStatus = region.data["Economic Status"]
                let employed = this.percentage(econStatus, ["Employed"])

                let educationAttending = region.data["Education Attending"]
                let edu = this.percentage(educationAttending, ["Tertiary", "University"]) 

                let householdSize = region.data["Household Size"]
                let hhs = this.percentage(householdSize, ["Medium [4-6]", "High [7+]"])

                let householdMonthlyIncome = region.data["Household Monthly Income Work"]
                let hmilow = this.percentage(householdMonthlyIncome, ["Low [0-5000]"])
                let hmimid = this.percentage(householdMonthlyIncome, ["Middle [5000-10000]"])
                let hmihigh = this.percentage(householdMonthlyIncome, ["High [10000+]"])


                let income = region.data["Income From Work"]
                let ilow = this.percentage(income, ["Low [0-3000]"])
                let imid = this.percentage(income, ["Middle [3000-6000]"])
                let ihigh = this.percentage(income, ["High [6000+]"])


                let ageGroup = region.data["Population Age Group"]
                let age19 = this.percentage(ageGroup, ["0-19"])
                let age39 = this.percentage(ageGroup, ["20-39"])
                let age59 = this.percentage(ageGroup, ["40-59"])
                let age60 = this.percentage(ageGroup, ["60+"])

                return `
                    % employed: ${employed}% <br>
                    % tertiary education & above: ${edu}% <br>
                    % household size [4 and above]: ${hhs}% <br>
                    % household monthly income low [0-5000]: ${hmilow}% <br>
                    % household monthly income middle [5000-10000]: ${hmimid}% <br>
                    % household monthly income high [10000+]: ${hmihigh}% <br>
                    % monthly income low [0-3000]: ${ilow}% <br>
                    % monthly income middle [3000-6000]: ${imid}% <br>
                    % monthly income high [6000+]: ${ihigh}% <br>
                    % age group [0-19]: ${age19}% <br>
                    % age group [20-39]: ${age39}% <br>
                    % age group [40-59]: ${age59}% <br>
                    % age group [60+]: ${age60} <br>
                `
            }

            catch {
                return `
                    Data not available!
                `
            }
        },

    },


    watch: {

        selectedRegions: function (n, o) {
            console.log("WATCHIN", n, o)
        }


    }



}

</script>