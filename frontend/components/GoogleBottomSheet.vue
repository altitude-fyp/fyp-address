<template>
  <!--This is the bottom sheet-->
  <div class="text-center">

    <v-bottom-sheet v-model="this.sheet"
                    persistent
                    :hide-overlay=true
    >
      <v-sheet class="text-center pl-16" height="400px">
        <v-btn
          class="mt-6"
          text
          color="error"
          @click="$emit('click')"
        >close
        </v-btn>

        <div class="py-3">{{ this.details }}</div>

        <v-row class="text-left">
          <v-col>
            <h3>At a Glance</h3>
          </v-col>
        </v-row>

        <v-row class="text-left">
          <v-col>
            <h4>Household Type</h4>
            <v-list>
              <v-list-item>
                <v-row>
                  <v-col>
                    <h4>HDB</h4>
                  </v-col>
                  <v-col>
                    {{ retrievedCity.hdb }}
                  </v-col>
                </v-row>
              </v-list-item>
              <v-list-item>
                <h4>Condos</h4>{{ retrievedCity.condo }}
              </v-list-item>
              <v-list-item>
                <h4>Landed</h4>{{ retrievedCity.landed }}
              </v-list-item>
            </v-list>
          </v-col>
          <v-divider vertical inset></v-divider>
          <v-col>

          </v-col>
          <v-divider vertical></v-divider>
          <v-col>
            <h4>Mode of Transport(Work)</h4>
          </v-col>
        </v-row>
        <v-divider></v-divider>
      </v-sheet>

    </v-bottom-sheet>
  </div>
</template>

<script>
export default {
  name: "GoogleBottomSheet",
  props: ['details', 'sheet'],
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
    }
  },
  methods: {
    onClickButton() {
      this.$emit('click')
    }
  }
}
</script>

<style scoped>

</style>
