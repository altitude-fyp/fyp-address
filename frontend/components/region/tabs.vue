<template>
  <v-container>
    <v-tabs
      v-model="tab"
      background-color="transparent"
      fixed-tabs
    >
      <v-tab
        v-for="item in items"
        :key="item"
      >
        <v-icon style="padding-right: 8px;">{{item.icon}}</v-icon> {{ item.header }}

      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item><!--First Tab Content-->
        <v-card
          flat
        >
          <v-card-text>TEXT 1</v-card-text>
        </v-card>
      </v-tab-item> <!--First Tab Content-->
      <v-tab-item><!--Second Tab Content-->
        <v-card
          flat
        >
          <v-card-text>TEXT 2</v-card-text>
        </v-card>
      </v-tab-item><!--Second Tab Content-->
      <v-tab-item><!--Third Tab Content-->
        <v-card
          flat
        >
          <v-card-text>TEXT 3</v-card-text>
        </v-card>
      </v-tab-item><!--Third Tab Content-->
      <v-tab-item><!--Fourth Tab Content-->
        <v-card
          flat
        >
          <v-card-text>TEXT 4</v-card-text>
        </v-card>
      </v-tab-item><!--Fourth Tab Content-->

    </v-tabs-items>
  </v-container>
</template>

<script>
export default {
  name: "tabs",
  data() {
    return {
      tab: null,
      items: [
        {
          header: 'At a Glance',
          icon: 'mdi-magnify-scan'
        },
        {
          header: 'Economy',
          icon: 'mdi-earth'
        },
        {
          header: 'Society',
          icon: 'mdi-handshake'
        },
        {
          header: 'Household',
          icon: 'mdi-home'
        }]
    }
  }
  ,
}
</script>

<style scoped>

</style>
