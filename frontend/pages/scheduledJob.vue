<template>
  <v-app>
  <v-container>

    <!-- Table Name -->
    <v-row class="firstrow">
      <div class="h2-text">
          <h2>Scheduled Jobs</h2>
      </div>
    </v-row>

    <v-data-table
      :headers="headers"
      :items="scheduledJobs"
      :search="search"
      sort-by="calories"
      class="elevation-1"
    >
      <template v-slot:top>
        <br/>
        <!-- Search -->
        <v-toolbar flat color="white" style="height:80px;">
          <div class="searchBar">
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            hide-details
            single-line
            style="width: 300px;"
          />
          </div>

        <!-- New Schedule CTA -->
        <v-spacer></v-spacer>
        <v-dialog v-model="dialog" max-width="500px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              color="#004D8E"
              class="white--text mb-2"
              large
              depressed
              v-bind="attrs"
              v-on="on"
            >+ New Schedule</v-btn>
          </template>

          <!-- Form Fields -->
          <v-card>
            <div class="modalHeader">
              <v-row>
                <v-layout align-center style="margin-left:15px; margin-right:15px;">
                  <v-col>
                    <v-card-title class="ma-0 pa-3">
                        {{ formTitle }}
                    </v-card-title>
                  </v-col>

                  <v-col class="text-right">
                    <v-btn icon dark @click="dialog = false">
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </v-col>
                </v-layout>

              </v-row>
            </div>
            <v-divider class="modal"></v-divider><br/>

            <v-card-text>
              <div class="form-fields">
                <!-- Job Name -->
                <v-row>
                  <h3>Job Name</h3>
                </v-row>
                <v-row>
                  <v-text-field v-model="editedItem.jobName" class="ma-0 pa-0" placeholder="Name for your job"/>
                </v-row><br/>

                <!-- Type -->
                <v-row>
                  <h3>Type</h3>
                </v-row>
                <v-row>
                  <v-radio-group row v-model="radios" :mandatory="false">
                    <v-radio color="#004D8E" label="Customers" value="radio-1"/>
                    <v-radio color="#004D8E" label="Merchants" value="radio-2"/>
                  </v-radio-group>
                 </v-row><br/>

                <!-- Frequency -->
                <v-row>
                  <h3>Frequency</h3>
                </v-row>
                <v-row>
                  <v-select class="ma-0 pa-0" v-model="frequencySelected" :items="frequency"/>
                </v-row><br/>

                <!-- Date Picker -->
                <v-row>
                  <h3>Next Run Date</h3>
                </v-row>
                <v-row>
                  <v-menu
                    v-model="menu2"
                    :close-on-content-click="false"
                    :nudge-right="40"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                  >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date"
                      label="Select a date"
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker color="#004D8E" v-model="date" @input="menu2 = false"></v-date-picker>
                  </v-menu>
                </v-row><br/>

                <!-- Time Picker -->
                <v-row>
                  <h3>Next Run Time</h3>
                </v-row>
                <v-row>
                  <v-flex>
                    <v-select class="ma-0 pa-0" :items="selectHour" placeholder="Hour"></v-select>
                  </v-flex>
                  <v-flex></v-flex>
                    <v-select class="ma-0 pa-0" :items="selectMinute" placeholder="Minute"></v-select>
                  </v-flex>
                </v-row><br/>

                <!-- Email Address -->
                <v-row>
                  <h3>Email Address</h3>
                </v-row>
                <v-row>
                  <v-combobox
                    v-model="chips"
                    :items="emails"
                    class="ma-0 pa-0"t
                    clearable
                    placeholder="Enter one or multiple email addresses"
                    multiple
                  >
                    <template v-slot:selection="{ attrs, item, select, selected }">
                      <v-chip
                        v-bind="attrs"
                        color="#004D8E"
                        class="white--text"
                        :input-value="selected"
                        close
                        @click="select"
                        @click:close="remove(item)"
                      >
                        <strong>{{ item }}</strong>&nbsp;
                      </v-chip>
                    </template>
                  </v-combobox>
                </v-row>
              </div>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-flex text-xs-center align-center>
                <v-btn class="save-btn" outlined color="#004D8E" @click="close">Cancel</v-btn>
                <v-btn class="save-btn white--text" color="#004D8E" large depressed @click="save">Save</v-btn><br/><br/><br/>
              </v-flex>
            </v-card-actions>
          </v-card>
          </v-dialog>
        </v-toolbar>
      </template>

      <!-- Actions -->
      <template v-slot:item.actions="{ item }">
        <v-icon
          small
          class="mr-2"
          @click="editItem(item)"
        >
          mdi-pencil
        </v-icon>
        <v-icon
          small
          @click="deleteItem(item)"
        >
          mdi-delete
        </v-icon>
      </template>

      <template v-slot:no-data>
        <v-btn color="primary" @click="initialize">Reset</v-btn>
      </template>

    </v-data-table>
  </v-container>
  </v-app>
</template>

<script>
  export default {
    data: () => ({
      dialog: false,
      radios: 'radio-1',
      frequencySelected: "Monthly",
      frequency: ["Hourly","Daily","Monthly","Bi-Monthly","Quarterly","Yearly"],
      chips: [],
      selectHour: ["00","01","02","03","04","05","05","06"],
      selectMinute: ["00","15","30","45"],
      date: new Date().toISOString().substr(0, 10),
      headers: [
        {
          text: 'Job Name',
          align: 'start',
          value: 'jobName',
        },
        { text: 'Type', value: 'type' },
        { text: 'Frequency', value: 'frequency' , sortable: false},
        { text: 'Next Run Date', value: 'nextRunDate' , sortable: false},
        { text: 'Next Run Time', value: 'nextRunTime' , sortable: false},
        { text: 'Email', value: 'email' , sortable: false},
        { text: 'Actions', value: 'actions' , sortable: false},
      ],
      scheduledJobs: [],
      editedIndex: -1,
      editedItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      defaultItem: {
        name: '',
        calories: 0,
        fat: 0,
        carbs: 0,
        protein: 0,
      },
      search: '',
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'New Schedule' : 'Edit Schedule'
      },
    },

    watch: {
      dialog (val) {
        val || this.close()
      },
    },

    created () {
      this.initialize()
    },

    methods: {
      initialize () {
        this.scheduledJobs = [
          {
            jobName: "Singapore Cust 2020",
            type: "Customers",
            frequency: "Monthly",
            nextRunDate: "26 Sep 2020",
            nextRunTime: "01:30 AM",
            email: "xavierlur@citi.com"
          },
          {
            jobName: "MY Merchant Data",
            type: "Merchants",
            frequency: "Bi-monthly",
            nextRunDate: "03 Oct 2020",
            nextRunTime: "03:30 AM",
            email: "xavierlur@citi.com"
          },
          {
            jobName: "UK Customer Add",
            type: "Customers",
            frequency: "Daily",
            nextRunDate: "07 Sep 2020",
            nextRunTime: "03:15 AM",
            email: "xavierlur@citi.com"
          },
          {
            jobName: "Addresses (TH)",
            type: "Customers",
            frequency: "Monthly",
            nextRunDate: "29 Sep 2020",
            nextRunTime: "12:00 AM",
            email: "xavierlur@citi.com"
          },
          {
            jobName: "SG Merchant Data",
            type: "Merchants",
            frequency: "Quarterly",
            nextRunDate: "30 Oct 2020",
            nextRunTime: "02:00 AM",
            email: "xavierlur@citi.com"
          },
        ]
      },

      editItem (item) {
        this.editedIndex = this.scheduledJobs.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.scheduledJobs.indexOf(item)
        confirm('Are you sure you want to remove this scheduled job?') && this.scheduledJobs.splice(index, 1)
      },

      close () {
        this.dialog = false
        this.$nextTick(() => {
          this.editedItem = Object.assign({}, this.defaultItem)
          this.editedIndex = -1
        })
      },

      save () {
        if (this.editedIndex > -1) {
          Object.assign(this.scheduledJobs[this.editedIndex], this.editedItem)
        } else {
          this.scheduledJobs.push(this.editedItem)
        }
        this.close()
      },

      remove (item) {
        this.chips.splice(this.chips.indexOf(item), 1)
        this.chips = [...this.chips]
      },
    },
  }
</script>

<!-- CSS-->
<style scoped>
  #app {
    background-color: #F4F7F9;
  }
  .row.firstrow {
    margin-bottom:20px;
  }
  .col {
    margin: 0 auto;
  }
  .container {
    margin-top:80px;
  }
  .v-btn {
    text-transform: none !important;
  }
  .h2-text {
    display : inline-flex;
    margin-left: 15px;
  }
  .searchBar {
    display : inline-flex;
  }
  .v-data-table
  /deep/
  tbody
  /deep/
    tr:hover:not(.v-data-table__expanded__content) {
      background: #F2F9FE !important;
  }
  .modalHeader {
    background-color: #063A66;
    color: #fff;
  }
  .form-fields {
    margin-left: 20px;
    margin-right:20px;
  }
  .form-fields h3 {
    margin-bottom: 10px;
  }
  .v-input--selection-controls {
    margin: 0 !important;
  }
  .v-btn.save-btn {
    min-width: 120px;
    min-height: 45px;
    margin-left: 5px;
    margin-right: 5px;
  }
</style>