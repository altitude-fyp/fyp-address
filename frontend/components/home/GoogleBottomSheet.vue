<template>
  <v-row>
    <v-col cols="3">

      <v-card
        class="mx-auto"
        outlined
      >
        <v-list-item>

          <v-list-item-avatar
            size="100"
            tile
            style="padding-top:10px"
          >
            <img src="@/assets/SingaporeFlag.png"/>
          </v-list-item-avatar>
            <div class="overline mb-4" >SINGAPORE</div>

        </v-list-item>

      </v-card>

      <v-card class="mx-auto"
              outlined>
        <v-col style="padding-top:20px;">
          <v-row style="padding-bottom: 8px;" justify="center">
            <v-btn small outlined color="primary" @click="dialog = true, access= 'Regions'">Select Regions in Singapore</v-btn>
          </v-row>

          <v-row style="padding-bottom: 8px;" justify="center">
            <v-btn small outlined color="primary" @click="dialog = true, access= 'Countries'">Select Countries to Compare</v-btn>
          </v-row>

          <v-row justify="center">
            <v-btn small outlined color="primary" @click="">Filter By</v-btn>
          </v-row>

        </v-col>
      </v-card>
    </v-col>

    <v-col cols="9">
      <v-card class="mx-auto">
        <v-container>
          <v-row>
            <v-col cols="3">
              <v-row>
                <v-col>
                  <v-card-subtitle>Total GDP :</v-card-subtitle>
                  <v-card-text style="font-size: 16px;">S${{ retrievedCountry.total }} billion</v-card-text>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-subtitle>Per Capital : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">S${{ retrievedCountry.percap }}</v-card-text>
                </v-col>
              </v-row>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="2.5">
              <v-row>
                <v-col>
                  <v-card-subtitle>Gini : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.gini }}</v-card-text>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-subtitle>HDI : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.hdi }}</v-card-text>
                </v-col>
              </v-row>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="3">
              <v-row>
                <v-col>
                  <v-card-subtitle>Inflation Rate : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.inflation }}</v-card-text>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-subtitle>Employed Persons : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.employed }} million
                  </v-card-text>
                </v-col>
              </v-row>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="3">
              <v-row>
                <v-col>
                  <v-card-subtitle>Population : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.pop }} millions</v-card-text>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-subtitle>Area : </v-card-subtitle>
                  <v-card-text style="font-size: 16px;">{{ retrievedCountry.area }} km</v-card-text>
                </v-col>
              </v-row>
            </v-col>
          </v-row>
        </v-container>
      </v-card>
    </v-col>
    <country-region :dialog="dialog" :access="access"  @close="onClose"/>
  </v-row>

</template>

<script>
import CountryRegion from "@/components/home/CountryRegion";

export default {
  name: "GoogleBottomSheet",
  components: {CountryRegion},
  props: {
    dialog: Boolean,
    access: String
  },
  data() {
    return {
      retrievedCity: {
        city: 'Ang Mo Kio',
        hdb: 70258,
        condo: 15022,
        landed: 2801,
        employed: 40155,
        unemployment: '2.17%',
        household: '5500',
        bus: 40118,
        mrt: 39023,
        car: 2801,
        taxi: 5221,
        motor: 3123,
        lorry: 543
      },
      retrievedCountry: {
        city: 'Singapore',
        total: 70258,
        percap: 15022,
        gini: 45.9,
        hdi: 0.935,
        inflation: '2.17%',
        employed: '3.54',
        pop: 57.1,
        area: 725.7,
      },
    }
  },
  methods: {
    onClose(anything) {
      this.dialog = false;
      console.log(anything)
    }
  }
}
</script>

<style scoped>

</style>
