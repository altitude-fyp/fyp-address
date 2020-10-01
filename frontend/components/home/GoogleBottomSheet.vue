<template>
  <v-container v-if="isLoaded">
    <v-row>
      <v-col cols="3">

        <v-card
          class="mx-auto"
          outlined
        >
          <div v-if='countries.length === 1'>
            <v-row class="mx-auto">
              <v-col class="mx-auto">
                <div class="mx-auto">{{ countries[0] }}</div>
              </v-col>
            </v-row>
            <v-row>
              <v-img :src="Tags.data.flag[0]" aspect-ratio="2" contain/>
            </v-row>

          </div>
          <div v-else>
            <div v-for="flagAccess in Tags.data.flag">
              <v-row class="mx-auto">
                <v-col class="mx-auto">
                  <div :class="'overline' && colors[Tags.data.flag.indexOf(flagAccess)]">
                    {{ countries[Tags.data.flag.indexOf(flagAccess)] }}
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <v-img :src="flagAccess" aspect-ratio="2" contain/>
              </v-row>


            </div>
          </div>

          <v-row class="mx-auto">
            <v-col>
              <div class="overline mb-4" v-if="access==='Region'">
                REGION COMES HERE
              </div>
            </v-col>
          </v-row>
          <v-divider></v-divider>

          <v-col style=" padding-top:20px;">
            <!-- <div v-if="countries.length === 1">
              <v-row style="padding-bottom: 8px;" justify="center">
                <v-btn small outlined color="primary" @click="dialog = true, access= 'Region'">Select Regions in
                  {{ countries[0] }}
                </v-btn>
              </v-row>
            </div> -->

            <v-row style="padding-bottom: 20px;" justify="center">
              <v-btn small outlined color="primary" @click="dialog = true, access= 'Countries'">Select Countries to
                Compare
              </v-btn>
            </v-row>
          </v-col><!-- Region/Country btn-->
          <v-divider></v-divider>

          <v-list
            subheader
            flat
          >
            <v-list-item-group
              v-model="selectTags"
              multiple
            >
              <v-row style="padding-top: 8px;" justify="center">
                <v-btn @click="selectTags = []" outlined small>Clear Filter</v-btn>
              </v-row> <!--Clear Filter btn-->

              <div v-for="item in Tags.data.filter">

                <v-subheader>{{ item.category }}</v-subheader>
                <div v-for="tag in item.value">
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
          </v-list> <!--Filter data checklist-->

        </v-card>

      </v-col>
      <v-col cols="9">
        <v-card class="mx-auto">
          <v-container>
            <v-row>

              <!-- CAN WE PUT TTHIS IN A FOR LOOP WTF -->
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 1">
                    <v-card-subtitle> {{ Tags.data.top8[0].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[0].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[0].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[0].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[0].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[0]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[0]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[0]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[0]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[0]].value[3] }}
                    </v-card-text>
                  </v-col>

                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>

              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 2">
                    <v-card-subtitle> {{ Tags.data.top8[1].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[1].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[1].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[1].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[1].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[1]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[1]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[1]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[1]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[1]].value[3] }}
                    </v-card-text>
                  </v-col>

                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>

              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 3">
                    <v-card-subtitle> {{ Tags.data.top8[2].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[2].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[2].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[2].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[2].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[2]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[2]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[2]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[2]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[2]].value[3] }}
                    </v-card-text>
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>

              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 4">
                    <v-card-subtitle> {{ Tags.data.top8[3].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[3].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[3].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[3].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[3].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[3]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[3]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[3]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[3]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[3]].value[3] }}
                    </v-card-text>
                  </v-col>
                </v-row>
              </v-col>

            </v-row>
            <v-row>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 5">
                    <v-card-subtitle> {{ Tags.data.top8[4].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[4].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[4].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[4].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[4].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[4]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[4]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[4]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[4]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[4]].value[3] }}
                    </v-card-text>
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 6">
                    <v-card-subtitle> {{ Tags.data.top8[5].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[5].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[5].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[5].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[5].value[3]
                      }}
                    </v-card-text>

                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[5]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[5]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[5]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[5]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[5]].value[3] }}
                    </v-card-text>
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 7">
                    <v-card-subtitle> {{ Tags.data.top8[6].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[6].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[6].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[6].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[6].value[3]
                      }}
                    </v-card-text>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[6]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[6]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[6]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[6]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3] " style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[6]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 8">
                    <v-card-subtitle> {{ Tags.data.top8[7].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.top8[7].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">{{
                        Tags.data.top8[7].value[1]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">{{
                        Tags.data.top8[7].value[2]
                      }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">{{
                        Tags.data.top8[7].value[3]
                      }}
                    </v-card-text>

                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle>{{ Tags.data.items[selectTags[7]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[7]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[7]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[7]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[7]].value[3] }}
                    </v-card-text>

                  </v-col>
                </v-row>
              </v-col>
            </v-row>

          </v-container>
        </v-card> 
        
        
        <!--Top 8 features-->
        <!-- CAN WE ALSO REFACTOR THIS INTO A FOR LOOP PLS AFTER MIDTERMS -->
        <v-card style="margin-top: 45px" class="mx-auto" v-if="selectTags.length > 8">
          <v-container>
            <v-row>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 8">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[8]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[8]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[8]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[8]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[8]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 9">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[9]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[9]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[9]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[9]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[9]].value[3] }}
                    </v-card-text>
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 10">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[10]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[10]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" tyle="font-size: 16px;">
                      {{ Tags.data.items[selectTags[10]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[10]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[10]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 11">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[11]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[11]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[11]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[11]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[11]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
            </v-row>

            <v-row>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 12">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[12]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[12]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[12]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[12]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[12]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 13">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[13]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[13]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[13]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[13]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[13]].value[3] }}
                    </v-card-text>

                  </v-col>

                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 14">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[14]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[14]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[14]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[14]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[14]].value[3] }}
                    </v-card-text>

                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
              <v-col cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 15">
                    <v-card-subtitle>{{ Tags.data.items[selectTags[15]].name }}</v-card-subtitle>
                    <v-card-text style="font-size: 16px;">{{ Tags.data.items[selectTags[15]].value[0] }}</v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 1" :class="colors[1]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[15]].value[1] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 2" :class="colors[2]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[15]].value[2] }}
                    </v-card-text>
                    <v-card-text v-if="Tags.data.flag.length > 3" :class="colors[3]" style="font-size: 16px;">
                      {{ Tags.data.items[selectTags[15]].value[3] }}
                    </v-card-text>
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>

            </v-row>
          </v-container>
        </v-card> <!--Next 8 features-->
        <div v-if="selectTags.length === 16" style="text-align: center; margin-top:40px">

          You have selected the maximum number of features (16) to display

        </div> <!--Max features selected notification-->
        <v-card class="mx-auto" style="margin-top:30px;">
          <v-container v-if="getTopThree === true">
            <v-row>
              <v-col cols="3.5">
                <v-row class="mx-auto">
                  <img :src="topThree.data.items[0].flag" aspect-ratio="1.7" contain @click="() => topThreeOnClose(topThree.data.items[0].name)"/>
                  <v-subheader>{{ topThree.data.items[0].name }}</v-subheader>
                </v-row>
                <v-row class="mx-auto">
                  <div class="overline text-decoration-underline">Score: {{ topThree.data.items[0].score }}</div>
                </v-row>
                <v-row class="mx-auto" v-for="listType in topThree.data.items[0].value">
                  <div class="overline">{{ listType }}</div>
                </v-row>
              </v-col>
              <v-divider vertical></v-divider>

               <v-col cols="3.5">
                 <v-row class="mx-auto">
                   <img :src="topThree.data.items[1].flag" aspect-ratio="1.7" @click="() => topThreeOnClose(topThree.data.items[1].name)" contain/>
                   <v-subheader>{{ topThree.data.items[1].name }}</v-subheader>
                 </v-row>
                 <v-row class="mx-auto">
                   <div class="overline text-decoration-underline">Score: {{ topThree.data.items[1].score }}</div>
                 </v-row>
                 <v-row class="mx-auto" v-for="listType in topThree.data.items[1].value">
                   <div class="overline">{{ listType }}</div>
                 </v-row>
               </v-col>
               <v-divider vertical></v-divider>

               <v-col cols="3.5">
                 <v-row class="mx-auto">
                   <img :src="topThree.data.items[2].flag" aspect-ratio="1.7" @click="() => topThreeOnClose(topThree.data.items[2].name)" contain/>
                   <v-subheader>{{ topThree.data.items[2].name }}</v-subheader>
                 </v-row>
                 <v-row class="mx-auto">
                   <div class="overline text-decoration-underline">Score: {{ topThree.data.items[2].score }}</div>
                 </v-row>
                 <v-row class="mx-auto" v-for="listType in topThree.data.items[2].value">
                   <div class="overline">{{ listType }}</div>
                 </v-row>
               </v-col>

            </v-row>
          </v-container>
        </v-card>
      </v-col>

      <country-region :dialog="dialog" :access="access" @close="onClose"/>
    </v-row>

  </v-container>
</template>

<script>
import CountryRegion from "@/components/home/CountryRegion";
import GoogleMap from "@/components/home/GoogleMap";

export default {
  name: "GoogleBottomSheet",
  components: {CountryRegion, GoogleMap},
  props: {
    dialog: Boolean,
    access: String
  },
  data() {
    return {
      selectTags: [],
      Tags: null,
      isLoaded: false,
      getTopThree: false,
      data: null,
      topThree: null,
      countries: ['Singapore'],
      colors: ['black--text', 'blue--text', 'teal--text', 'blue-grey--text'],
    }
  },
  mounted() {
    this.getUserData();
  },
  methods: {
    topThreeOnClose(data) {
      this.$axios.$post('http://lzl.blue/api/countries/', {
        "countries": [data]
      }).then((Tags) => {
        this.Tags = Tags
        this.countries = [data]
        this.$emit('load-coordinates', this.Tags.data.coordinates)
      })
    },
    onClose(acceptance) {
      this.dialog = false;
      if (acceptance[0] !== 'close') {
        if (acceptance[0] === 'country') {
          this.countries = acceptance[1];
          this.$axios.$post('http://lzl.blue/api/countries/', {
            "countries": acceptance[1]
          }).then((Tags) => {
            this.Tags = Tags
            this.$emit('load-coordinates', this.Tags.data.coordinates)
          })
        } else {
          //REGION DATA POST
        }
      }
    },

    getUserData() {
      this.$axios.$post('http://lzl.blue/api/countries/', {
        "countries": [
          "Singapore"
        ]
      }).then((Tags) => {
        this.Tags = Tags
        this.isLoaded = true
        this.$emit('load-coordinates', this.Tags.data.coordinates)
      })
      this.$axios.$get('http://lzl.blue/api/analytics/top_countries/Singapore').then((topThree) => {
          this.topThree = topThree
          this.getTopThree = true
        }
      )
    },
  }
}
</script>

<style scoped>

</style>
