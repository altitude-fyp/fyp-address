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
            max-height="70px"
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



              <v-list
                dense
                v-if='access=="Region"'
              >
                <v-card
                  class="mx-auto"
                  max-width="800"
                  outlined

                >
                  <v-card-subtitle>You have selected the following regions for comparison:</v-card-subtitle>
                  <v-card-subtitle>{{regionSelect}}</v-card-subtitle>

                  <div style="padding:10px;">
                    <v-btn depressed  @click="regionSelect=[]">Reset All</v-btn>
                  </div>
                </v-card>

                <v-list-item style="padding-top: 80px">
                  <v-list-item-content v-if='access=="Region"' v-for='reg in region'>
                    <h3>{{ reg.title }}</h3>
                  <ul>
                    <v-checkbox v-model="regionSelect" v-for='dist in reg.include' :label='dist.place'
                                :value='dist.place'>
                    </v-checkbox>
        </ul>
                  </v-list-item-content>
                </v-list-item>
              </v-list>


          <v-list
            dense
          >
            <v-card
              class="mx-auto"
              max-width="800"
              outlined
              v-if='access=="Countries"'
            >
          <v-card-subtitle>You have selected the following countries for comparison:</v-card-subtitle>
              <v-card-subtitle>{{countrySelect}}</v-card-subtitle>

              <div style="padding:10px;">
                <v-btn depressed  @click="countrySelect=[]">Reset All</v-btn>
              </div>

            </v-card>
            <v-list-item style="padding-top: 80px">
              <v-list-item-content v-if='access=="Countries"' v-for='reg in country'>
                <h3>{{ reg.title }}</h3>
                <ul>
                  <v-checkbox v-model="countrySelect" v-for='dist in reg.include' :label='dist.place'
                              :value='dist.place'>
                  </v-checkbox>
                </ul>
              </v-list-item-content>
            </v-list-item>
          </v-list>


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
      n: 0,
      regionSelect: [],
      country: [
        {
          title: 'Africa', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'Asia',
          include: [
            {place: 'Alexandra Road'},
            {place: 'Tiong Bahru'},
            {place: 'Queenstown'},
            {place: 'RCR1'},
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Suntec City'},
          ]
        },
        {
          title: 'The Caribbean', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'Central America', include: [
            {place: 'Boat Quay2'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'Europe', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'North America', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'Oceania', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'South America', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
      ],
      region: [
        {
          title: 'Central Region', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'North Region',
          include: [
            {place: 'Alexandra Road'},
            {place: 'Tiong Bahru'},
            {place: 'Queenstown'},
            {place: 'RCR1'},
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
          ]
        },
        {
          title: 'North-East Region', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'East Region', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
        {
          title: 'West Region', include: [
            {place: 'Boat Quay'},
            {place: 'Chinatown'},
            {place: 'Havelock Road'},
            {place: 'Marina Square'},
            {place: 'Raffles Place'},
            {place: 'Suntec City'}
          ]
        },
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

