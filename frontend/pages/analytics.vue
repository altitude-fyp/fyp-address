<template>
  <v-app>
    <div style="padding-top: 50px">




      <v-container>
        <v-row dense>
          <v-col
          >
            <v-card>
              INFO 1
            </v-card>
          </v-col>

          <v-col
          >
            <v-card>
              INFO 2
            </v-card>
          </v-col>

          <v-col
          >
            <v-card>
              INFO 3
            </v-card>
          </v-col>
          <v-col
          >
            <v-card>
              INFO 4
            </v-card>
          </v-col>

        </v-row>

        <v-row dense>
          <v-col
          >
            <v-card>
              <line-chart/>
            </v-card>
          </v-col>

          <v-col
          >
            <v-card>
              <bar-chart/>
            </v-card>
          </v-col>

        </v-row>
      </v-container>


    </div>
  </v-app>

</template>

<script>
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";

export default {
  name: "analytics",
  components: {BarChart, lineChart},
};
</script>

<style scoped>

</style>
