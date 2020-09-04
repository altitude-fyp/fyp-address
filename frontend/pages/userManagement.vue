<template>
  <v-app>
  <v-container>

    <!-- Table Name -->
    <v-row class="firstrow">
      <div class="h2-text">
          <h2>User Management</h2>
      </div>
    </v-row>

    <v-data-table
      :headers="headers"
      :items="users"
      :search="search"
      sort-by="status"
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
            >+ Add User</v-btn>
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
                <!-- Name -->
                <v-row>
                  <h3>Name</h3>
                </v-row>
                <v-row>
                  <v-text-field v-model="editedItem.name" class="ma-0 pa-0" placeholder="Enter your name"/>
                </v-row><br/>

                <!-- Email -->
                <v-row>
                  <h3>Email</h3>
                </v-row>
                <v-row>
                  <v-text-field v-model="editedItem.email" class="ma-0 pa-0" placeholder="Enter your email"/>
                </v-row><br/>

                <!-- Location -->
                <v-row>
                  <h3>Location</h3>
                </v-row>
                <v-row>
                  <v-select class="ma-0 pa-0" v-model="locationSelected" :items="locations"/>
                </v-row><br/>

                <!-- Role -->
                <v-row>
                  <h3>Role</h3>
                </v-row>
                <v-row>
                  <v-select class="ma-0 pa-0" v-model="roleSelected" :items="roles"/>
                </v-row><br/>

                <!-- Status -->
                <v-row>
                  <h3>Status</h3>
                </v-row>
                <v-row>
                  <v-radio-group row v-model="radios" :mandatory="false">
                    <v-radio color="#004D8E" label="Active" value="radio-1"/>
                    <v-radio color="#004D8E" label="Inactive" value="radio-2"/>
                  </v-radio-group>
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

      <template v-slot:item.status="{ item }">
        <v-chip :color="getColor(item.status)" small dark>{{ item.status }}</v-chip>
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
      locationSelected: "Singapore",
      locations: ["Australia","China","France","Hong Kong","India","Singapore","United Kingdom","Vietnam"],
      roleSelected: "Data Analyst",
      roles: ["Admin","Data Analyst","Developer"],
      chips: [],
      selectHour: ["00","01","02","03","04","05","05","06"],
      selectMinute: ["00","15","30","45"],
      date: new Date().toISOString().substr(0, 10),
      headers: [
        {
          text: 'Name',
          align: 'start',
          value: 'name',
        },
        { text: 'Email', value: 'email' },
        { text: 'Location', value: 'location' , sortable: false},
        { text: 'Role', value: 'role' , sortable: false},
        { text: 'Status', value: 'status' , sortable: false},
        { text: 'Actions', value: 'actions' , sortable: false},
      ],
      users: [],
      editedIndex: -1,
      editedItem: {
        name: "",
        email: "",
        location: "",
        role: "",
        status: "",
      },
      defaultItem: {
        name: "",
        email: "",
        location: "",
        role: "",
        status: "",
      },
      search: "",
    }),

    computed: {
      formTitle () {
        return this.editedIndex === -1 ? 'Add User' : 'Edit User'
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
        this.users = [
          {
            name: "Xavier Lur",
            email: "xavier.lur@citi.com",
            location: "Singapore",
            role: "Admin",
            status: "Active",
          },
          {
            name: "David Thomas",
            email: "david.thomas@citi.com",
            location: "United Kingdom",
            role: "Admin",
            status: "Active",
          },
          {
            name: "Xi Min",
            email: "xi.min@citi.com",
            location: "China",
            role: "Data Analyst",
            status: "Active",
          },
          {
            name: "Ernest Chan",
            email: "ernest.chan@citi.com",
            location: "Hong Kong",
            role: "Developer",
            status: "Inactive",
          },
          {
            name: "Bang",
            email: "bang@citi",
            location: "Vietnam",
            role: "Data Analyst",
            status: "Inactive",
          },
        ]
      },

      editItem (item) {
        this.editedIndex = this.users.indexOf(item)
        this.editedItem = Object.assign({}, item)
        this.dialog = true
      },

      deleteItem (item) {
        const index = this.users.indexOf(item)
        confirm('Are you sure you want to remove this scheduled job?') && this.users.splice(index, 1)
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
          Object.assign(this.users[this.editedIndex], this.editedItem)
        } else {
          this.users.push(this.editedItem)
        }
        this.close()
      },

      remove (item) {
        this.chips.splice(this.chips.indexOf(item), 1)
        this.chips = [...this.chips]
      },

      getColor (status) {
        if (status == "Active") return 'green'
        else return 'red'
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