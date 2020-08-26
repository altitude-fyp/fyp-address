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
      <v-list-item class="px-2">

        <v-list-item-avatar>
          <v-img src="https://randomuser.me/api/portraits/men/85.jpg"></v-img>
        </v-list-item-avatar>

        <v-list-item-title style="color: white;">Xavier Lur </v-list-item-title>

        <v-btn
          icon
          @click.stop="mini = !mini"
        >
          <v-icon style="color: white;">mdi-chevron-left</v-icon>
        </v-btn>

      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
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
          link
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
        {title: 'Home', icon: 'mdi-home'},
        {title: 'Analytics', icon: 'mdi-chart-areaspline'},
        {title: 'Request History', icon: 'mdi-history'},
      ],
      items2: [
        {title: 'User Account', icon: 'mdi-account'},
        {title: 'Settings', icon: 'mdi-cog'},
      ],
      mini: true,
    }
  },
}
</script>


