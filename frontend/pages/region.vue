<template>
  <v-app>

    <!-- <region-map />
    <c-s-v-search/>
    <MetadataPanel/> -->
    <tabs :selectedRegions=selectedRegions />
    
  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";

export default {

  name: "region",
  
  components: {
  
    MetadataPanel,
    tabs,
    CSVSearch, 
    "region-map": RegionMap
  },

  data() {

    return {
      coordinates: null,
      selectedRegions: "ang mo kio,bishan"
    }

  },


  methods: {

  },


}
</script>
