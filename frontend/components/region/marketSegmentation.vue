<template>
  <v-container>
    <!--     HEADER -->
    <v-row>
      <!--      Market Segmentation header -->
      <v-col cols="5">
        <h1>
          <v-icon>mdi-filter
          </v-icon>
          Market Segmentation
        </h1>
      </v-col>

      <!--      Reset All Filter Button -->
      <v-col style="margin-top:15px; margin-left:-50px">
        <v-btn
          outlined
          color="#004D8E"
          class="mb-2"
          depressed
          small
          @click="none">
          Reset all filter
        </v-btn>
      </v-col>
    </v-row>

    <!--     PANELS -->
    <v-expansion-panels multiple>
      <v-expansion-panel
        v-for="(item,i) in items"
        :key="i">

        <v-expansion-panel-header><h3>{{ item }}</h3></v-expansion-panel-header>

        <!--        Content of the expansion-->
        <v-expansion-panel-content>
          <!-- For Economic Status and Population Age Group it will be a single checkbox-->
          <div v-if="!content[i]['slider']" v-for="j in content[i]['ticksLabels']" :key="j">
            <v-checkbox
              v-model="panel[i]"
              :label="j"
              :value="j"
            ></v-checkbox>
          </div>

          <!--           For Income related, it will be a slider-->
          <div v-if="content[i]['slider']">
            <v-slider
              v-model="panel[i]"
              :tick-labels="content[i]['ticksLabels']"
              :max="content[i]['max']"
              step="1"
              ticks="always"
              tick-size="6"
              thumb-size="24"
            ></v-slider>
          </div>

        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>

    <v-row>
      <v-col align="center"
             justify="center">
      <v-btn
        color="#004D8E"
        outlined
        class="mb-2"
        block
        depressed
        @click="none">
        Filter Data
      </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "marketSegmentation",
  data() {
    return {
      panel: [0, 0, 0, 0],
      items: ['Economic Status', 'Household Monthly Income Work', 'Income From Work', 'Population Age Group'],
      content: [
        {
          max: 1,
          slider: false,
          ticksLabels: [
            'Unemployed',
            'Employed',
          ],
        },
        {
          max: 2,
          slider: true,
          ticksLabels: [
            'Low Income',
            'Middle Income',
            'High Income',
          ]
        },
        {
          max: 2,
          slider: true,
          ticksLabels: [
            'Low Income',
            'Middle Income',
            'High Income',
          ]
        },
        {
          max: 5,
          slider: false,
          ticksLabels: [
            '20-30',
            '30-40',
            '40-50',
            '50-60',
            '60-70',
            '70-80'
          ]
        }],
    }
  },
  methods: {
    // Reset the panel
    none() {
      // panel will hold the values to be sent to backend and retrieved
      // Example of sending format : this.panel = [ "Employed", 1, 2, "40-50" ]
      this.panel = [0, 0, 0, 0]
    },
  },
}

</script>

<style scoped>

</style>
