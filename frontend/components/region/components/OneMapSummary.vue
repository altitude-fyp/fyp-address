<template>
    
    <div v-if="onemapSummaryData">
        {{ onemapSummaryData["Household Monthly Income Work"]["Percentage High Income [10000+]"] }}% of the population in Bishan are in the high income range compared to the Singapore average of  
        <br/><br/>
        {{ items }}
    </div>
     
</template>

<script>
export default {

    name: "onemap-summary",
    props: ["selectedRegions", "onemapSummaryData"],
    
    data() {
        return {

        items: [
            {
            employmentRate: 35,
            },
            {
            highIncomeRate: 25.5,
            },
        ]
        }
  },    
}

</script>

<style>

</style>