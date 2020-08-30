<template>
<!--  This is the navbar and also the main single page render-->
  <v-app>
    <v-navigation-drawer
      v-model="drawer"
      :mini-variant.sync="mini"
      color="primary"
      permanent
      app
    >

      <v-list dense>
        <v-list-item>
          <v-list-item-icon>
            <v-icon style="color: white;">mdi-menu</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title style="color: white;">CITILOGO GOES HERE</v-list-item-title>
          </v-list-item-content>
          <v-btn
            icon
            @click.stop="mini = !mini"
          >
            <v-icon style="color: white;">mdi-chevron-left</v-icon>
          </v-btn>
        </v-list-item>
      </v-list>


      <v-divider></v-divider>

      <v-list-item class="px-2">

        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>
``
        <v-list-item-title style="color: white;">HELP Lur </v-list-item-title>

      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.link"
          nuxt
        >
          <v-list-item-icon>
            <v-icon style="color: white;">{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title style="color: white;">{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items2"
          :key="item.title"
          :to="item.link"
        >

          <v-list-item-icon>
            <v-icon style="color: white;">{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title style="color: white;">{{ item.title }}</v-list-item-title>
          </v-list-item-content>


        </v-list-item>
      </v-list>

    </v-navigation-drawer>

    <!--This is the code to render the page do not remove-->
    <v-main style="padding: 0px;">
        <nuxt/>
    </v-main>
    <!--   -------    -->

  </v-app>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      items: [
        {title: 'Home', icon: 'mdi-home', link: '/home'},
        {title: 'Analytics', icon: 'mdi-chart-areaspline',link: '/analytics'},
        {title: 'Request History', icon: 'mdi-history',link: '/requestHistory'},
        {title: 'Notifications', icon: 'mdi-bell',link: '/notifications'},
      ],
      items2: [
        {title: 'User Account', icon: 'mdi-account',link: '/userAccount'},
        {title: 'Chatbot', icon: 'mdi-chat', link: '/chatbot'},
        {title: 'Settings', icon: 'mdi-cog', link: '/Settings'},
      ],
      mini: true,
    }
  },
}
</script>


