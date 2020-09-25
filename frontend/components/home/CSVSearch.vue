<template>
    <!--fluid style="padding-top: 400px; padding-left: 240px; position:absolute; z-index: 1;"-->
    <v-container >
      <v-row>
        <v-col cols="10">
          <v-text-field
            prepend-inner-icon="mdi-magnify"
            placeholder="Enter an address in full only"
            rounded
            solo
            v-on:keydown.enter="launchRadio = true"
          >
          </v-text-field>
        </v-col>

        <v-dialog persistent  v-model="launchRadio" max-width="600px">
            <v-card>
              <v-card-title>
                <span class="headline">Select Type of Address Queried</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-radio-group row v-model="choice" :mandatory="true">
                    <v-radio label="Customer" value="customer"></v-radio>
                    <v-radio label="Merchant" value="merchant"></v-radio>
                  </v-radio-group>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="launchRadio = false">Close</v-btn>
                <v-btn color="blue darken-1" text @click="launchRadio = false">Search</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>





        <v-col>
          <v-dialog v-model="dialog" persistent max-width="600px">
            <template v-slot:activator="{ on, attrs }">
              <v-btn
                color="primary"
                dark
                v-bind="attrs"
                v-on="on"
                :loading = 'loading'
                @click = 'loading = true'
                height="47"
              >
                <v-icon>mdi-application-import</v-icon> Import CSV
              </v-btn>
            </template>
            <v-card>
              <v-card-title>
                <span class="headline">Upload addresses in CSV</span>
              </v-card-title>
              <v-card-text>
                <v-container>
                  <v-file-input />
                  <v-radio-group row v-model="radios" :mandatory="true">
                    <v-radio label="Customer" value="customer"></v-radio>
                    <v-radio label="Merchant" value="merchant"></v-radio>
                  </v-radio-group>
                </v-container>
              </v-card-text>
              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn color="blue darken-1" text @click="dialog = false, loading = false">Close</v-btn>
                <v-btn color="blue darken-1" text @click="dialog = false, loading = false">Save</v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-col>
      </v-row>

    </v-container>

</template>

<script>
export default {
  name: "CSVSearch",
  data() {
    return {
      launchRadio: false,
      loading: false,
      radios: 'customer',
      dialog: false,
      choice: '',
      csvChoice: 'Customer',
      windowWidth: window.innerWidth,
    }
  },
  mounted() {
    window.onresize = () => {
      this.windowWidth = window.innerWidth
    }
  }
}
</script>

<style scoped>

</style>
