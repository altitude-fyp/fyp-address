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
          <v-btn justify-left outlined color="secondary" dark>Log Out</v-btn>
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
        {title: 'Analytics', icon: 'mdi-chart-areaspline',link: '/analytics'},
        {title: 'Scheduled Job', icon: 'mdi-history',link: '/scheduledJob'},
        {title: 'Notifications', icon: 'mdi-bell',link: '/notifications'},
        {title: 'User Management', icon: 'mdi-account',link: '/userManagement'},
        {title: 'Chatbot', icon: 'mdi-chat', link: '/chatbot'},
        {title: 'Settings', icon: 'mdi-cog', link: '/Settings'},
      ],
    }
  },
}
</script>
