<template>
  <div>
    <v-row
      justify="center"
    >

      <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
      >
        <v-card tile>
          <v-toolbar
            flat
            dark
            color="primary"
          >
            <v-btn
              icon
              dark
              @click="$emit('close','hello')"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Select {{ access }} for Comparison</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>
          <v-card-text>

            <v-list
              three-line
              subheader
            >
              <v-list-item>
                <v-list-item-content>
                  FOR LOOP FOR REGION AND COUNTRIES
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-card-text>

        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>


<script>
export default {
  name: "CountryRegion",
  props: {
    dialog: {
      type: Boolean,
    },
    access: {
      type: String,
    },
  },
  data() {
    return {
      countrySelect: [],
      countryRegion: '',
      regionSelect: [],
      country: [
        {label: "Country1", value: "Country1"},
        {label: "Country2", value: "Country2"},
        {label: "Country3", value: "Country3"},
        {label: "Country4", value: "Country4"},
        {label: "Country5", value: "Country5"},
        {label: "China", value: "China"},
        {label: "Japan", value: "Japan"},
        {label: "Korea", value: "Korea"},
        {label: "Singapore", value: "Singapore"},
        {label: "United States of America", value: "USA"},
        {label: "Country10", value: "Country1"},
        {label: "Country20", value: "Country2"},
        {label: "Country30", value: "Country3"},
        {label: "Country40", value: "Country4"},
        {label: "Country50", value: "Country5"},
      ],
      region: [
        {label: "Ang Mo Kio", value: "Country1"},
        {label: "Bishan", value: "Country2"},
        {label: "Braddell", value: "Country3"},
        {label: "Toa Payoh", value: "Country4"},
        {label: "Yio Chu Kang", value: "Country5"},
        {label: "Some Ulu", value: "China"},
        {label: "Somewhere Ulu", value: "Japan"},
        {label: "Kpop", value: "Korea"},
        {label: "Region1", value: "Region1"},


      ],
    }
  },
  methods: {
    resetDialog() {
      this.$emit('resetDialog', false)
    }
  },
}
</script>

