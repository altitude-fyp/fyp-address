<template>
  <v-container>
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
            <div class="overline mb-4">SINGAPORE</div>

          </v-list-item>

          <v-divider></v-divider>

          <v-col style=" padding-top:20px;">
            <v-row style="padding-bottom: 8px;" justify="center">

              <v-btn small outlined color="primary" @click="dialog = true, access= 'Region'">Select Regions in
                Singapore
              </v-btn>
            </v-row>

            <v-row style="padding-bottom: 20px;" justify="center">
              <v-btn small outlined color="primary" @click="dialog = true, access= 'Countries'">Select Countries to
                Compare
              </v-btn>
            </v-row>
          </v-col>
          <v-divider></v-divider>


          <v-list
            subheader
            flat
          >


            <v-list-item-group
              v-model="selectTags"
              multiple
            >
              <div v-for="item in tags">

                <v-subheader>{{ item.header }}</v-subheader>
                <div v-for="tag in item.type">
                  <v-list-item>
                    <template v-slot:default="{ active }">
                      <v-list-item-action>
                        <v-checkbox
                          :input-value="active"
                          color="primary"
                        ></v-checkbox>
                      </v-list-item-action>

                      <v-list-item-content>
                        <v-list-item-title>{{ tag }}</v-list-item-title>
                      </v-list-item-content>

                    </template>

                  </v-list-item>
                </div>
              </div>


            </v-list-item-group>
          </v-list>


        </v-card>

      </v-col>

      <v-col cols="9">
        <v-card class="mx-auto">
          <v-container>
            <v-row>
              <v-col cols="3">
                <v-row>

                  <v-col v-if="selectTags.length < 1">
                    <v-card-subtitle>{{tagsQuery[0].type}}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{tagsQuery[0].value}}</v-card-text>
                  </v-col>

                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[0]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[0]].value }} </v-card-text>
                  </v-col>

                </v-row>
                <v-row>

                  <v-col v-if="selectTags.length < 2">
                    <v-card-subtitle>{{tagsQuery[1].type}}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{tagsQuery[1].value}}</v-card-text>
                  </v-col>

                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[1]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[1]].value }} </v-card-text>
                  </v-col>

                </v-row>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="2.5">
                <v-row>
                  <v-col v-if="selectTags.length < 3">
                    <v-card-subtitle>{{tagsQuery[2].type}}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{tagsQuery[2].value}}</v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[2]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[2]].value }} </v-card-text>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col v-if="selectTags.length < 4">
                    <v-card-subtitle>{{tagsQuery[3].type}}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{tagsQuery[3].value}}</v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[3]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[3]].value }} </v-card-text>
                  </v-col>
                </v-row>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 5">
                    <v-card-subtitle>Inflation Rate :</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">HOLD</v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[4]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[4]].value }} </v-card-text>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col v-if="selectTags.length < 6">
                    <v-card-subtitle>HOLD</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">HOLD
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[5]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[5]].value }} </v-card-text>
                  </v-col>
                </v-row>
              </v-col>
              <v-divider vertical></v-divider>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 7">
                    <v-card-subtitle>HOLD:</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">HOLD</v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[6]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[6]].value }} </v-card-text>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col v-if="selectTags.length < 8">
                    <v-card-subtitle>HOLD</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">HOLD</v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ tagsQuery[selectTags[7]].type }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ tagsQuery[selectTags[7]].value }} </v-card-text>
                  </v-col>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
      <country-region :dialog="dialog" :access="access" @close="onClose"/>
    </v-row>
    <v-col cols="9">
      <v-row>
      </v-row>
    </v-col>

  </v-container>
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
      selectTags: [],
      tags: [
        {header: 'Economic Indicator', type: ['Total GDP', 'Per Capital', 'Gini', 'HDI',]},
        {header: 'Population Information', type: ['Inflation Rate', 'Employed Persons', 'Population',]},
        {header: 'Location Information', type: ['Area']},
      ],
      tagsQuery: [
        {type: 'Total GDP (S$ Billion)', value: 2},
        {type: 'Per Capital (S$ Billion) ', value: 3},
        {type: 'Gini', value: 4},
        {type: 'HDI', value: 5},
        {type: 'Inflation Rate (%) ', value: 6},
        {type: 'Employed Persons (Person)', value: 7},
        {type: 'Population', value: 8},
        {type: 'Area (Km)', value: 9},
      ]
    }
  },
  asyncData({$axios}) {
    return $axios.$get(`http://lzl.blue/api/filter/Singapore/`)
      .then((tagsDb) => {
        return {
          tagsDb // Put inside an object
        }
      })
  },
  methods: {
    onClose(anything) {
      this.dialog = false;
      console.log(anything)
    },
  }
}
</script>

<style scoped>

</style>
