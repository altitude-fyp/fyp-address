<template>
  <v-app>

      <v-card>
        <v-app-bar
          absolute
          color="white"

        >
          <v-app-bar-nav-icon  @click="drawer = true"></v-app-bar-nav-icon>

          <v-toolbar-title>{{ username }}</v-toolbar-title>

          <v-spacer></v-spacer>

          <v-menu
            bottom
            offset-y
            origin="top right"
            transition="scale-transition"
            max-width="400px"
          >

            <template v-slot:activator="{ attrs, on }">
              <v-btn
                class="ml-2"
                min-width="0"
                text
                v-bind="attrs"
                v-on="on"
              >
                <v-badge
                  color="red"
                  overlap
                  bordered
                >
                  <template v-slot:badge>
                    <span>{{ notifications.length }}</span>
                  </template>

                  <v-icon>mdi-bell</v-icon>
                </v-badge>
              </v-btn>
            </template>

            <v-list>
            
              <v-list-item-content>
                <div class="notifications">
                  <h3>Notifications</h3>
                </div>
              </v-list-item-content>
          

              <v-divider></v-divider>

              <div  class="notification_row">
              <v-list-item
                v-for="(notification, index) in notifications"
                :key="index"
                @click=""
              >

                <v-list-item-title v-if="index === 0">
                  <v-row style="margin:0">
                    <v-layout align-center>
                    <v-col>
                      <strong>{{ notification.filename }}</strong> {{ notification.title }}
                    </v-col>
                    <v-col class="shrink text-right">
                      <v-btn 
                        href="/analytics"
                        color="#004D8E"
                        class="white--text mb-2"
                        depressed
                      >
                      View</v-btn>
                    </v-col>
                    </v-layout>
                  </v-row>

                  <v-row style="margin:0">
                    <v-col style="margin-top:-15px">
                      <span style="font-size:13px;margin-bottom:20px;color:#757575">{{ notification.date }}</span>
                    </v-col>
                  </v-row>
                </v-list-item-title>

                <v-list-item-title v-if="index !== 0">
                  <v-row style="margin:0">
                    <v-layout align-center>
                    <v-col>
                      <strong>{{ notification.filename }}</strong> {{ notification.title }}
                    </v-col>
                    </v-layout>
                  </v-row>

                  <v-row style="margin:0">
                    <v-col style="margin-top:-15px">
                      <span style="font-size:13px;margin-bottom:20px;color:#757575">{{ notification.date }}</span>
                    </v-col>
                  </v-row>
                </v-list-item-title>
              </v-list-item>
              </div>
            </v-list>

          </v-menu>

          <div class="logout">
            <v-btn justify-left outlined color="secondary" dark>Log Out</v-btn>
          </div>
        </v-app-bar>

        <v-navigation-drawer
          v-model="drawer"
          absolute
          temporary
        >

          <v-list
            nav
            dense
          >
            <v-list-item>
              <v-list-item-avatar>
                <v-img src="https://cdn.vuetifyjs.com/images/john.png"></v-img>
              </v-list-item-avatar>
            </v-list-item>

            <v-list-item link>
              <v-list-item-content>
                <v-list-item-title class="title">{{ username }}</v-list-item-title>
                <v-list-item-subtitle>john@vuetifyjs.com</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-divider></v-divider>


            <v-list-item-group
              active-class="deep-blue--text text--accent-4"
              v-model="selectNav"
            >
              <v-list-item
                v-for="(item, i) in items"
                :key="i"
                :to="item.link">
                <v-list-item-icon>
                  <v-icon>{{item.icon}}</v-icon>
                </v-list-item-icon>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item>
            </v-list-item-group>

          </v-list>

        </v-navigation-drawer>

          <v-sheet style="padding-top: 50px;">
            <!--This is the code to render the page do not remove-->
            <v-main>
              <nuxt/>
            </v-main>
          </v-sheet>


      </v-card>




  </v-app>
</template>

<style>
  .notifications {
    margin-left: 28px !important;
  }
  .notification_row.v-list-item {
    min-height: 80px !important;
  }
  .v-list-item__title {
    white-space: normal !important;
    margin-top: 10px !important;
    margin-bottom: 10px !important;
  }
  .v-btn {
    text-transform: none !important;
  }
  .logout {
    margin-left:20px;
  }
</style>

<script>
export default {
  data() {
    return {
      selectNav: 1,
      drawer: false,
      username: 'Xavier Lur',
      activeBtn: 0,
      items: [
        {title: 'Home', icon: 'mdi-home', link: '/'},
        // {title: 'Analytics', icon: 'mdi-chart-areaspline',link: '/analytics'},
        // {title: 'Scheduled Job', icon: 'mdi-history',link: '/scheduledJob'},
        // {title: 'Notifications', icon: 'mdi-bell',link: '/notifications'},
        // {title: 'User Management', icon: 'mdi-account',link: '/userManagement'},
        // {title: 'Chatbot', icon: 'mdi-chat', link: '/chatbot'},
        // {title: 'Settings', icon: 'mdi-cog', link: '/Settings'},
      ],
      notifications: [
        {
          filename: "address_cust_1234.csv",
          title: " has been processed successfully",
          date: "2 hours ago",
        },
        {
          filename: "address_cust_1235.csv",
          title: " has been processed successfully",
          date: "3 hours ago",
        },
        {
          filename: "address_merchant_1235.csv",
          title: " has been processed successfully",
          date: "4 hours ago",
        },
        {
          filename: "address_merchant_SG.csv",
          title: " has been processed successfully",
          date: "1 day ago",
        },
      ],
    }
  },
}
</script>
