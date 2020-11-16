<template>

    <!-- 1 region is selected -->
    <div v-if="onemapSummaryData">
        <div v-if="selectedRegions.length === 1">
            <span v-if="selectedRegionHighIncomeRate[0] > SGhighIncomeRate">
                <span class="regionName">{{selectedRegions[0]}}</span> has a higher percentage of individual high income earners at <span class="regionValues">{{selectedRegionHighIncomeRate[0]}}%</span> compared to the overall Singapore average of <span class="regionValues">{{SGhighIncomeRate}}%</span>.
            </span>

            <span v-else>
                <span class="regionName">{{selectedRegions[0]}}</span> has a lower percentage of individual high income earners at <span class="regionValues">{{selectedRegionHighIncomeRate[0]}}%</span> compared to the overall Singapore average of <span class="regionValues">{{SGhighIncomeRate}}%</span>.
            </span>

            <span v-if="selectedRegionoldAgeGroupRate[0] > SGoldAgeGroupRate">
                It also has an older population with <span class="regionValues">{{selectedRegionoldAgeGroupRate[0]}}%</span> who are 60 years old and above, compared to the overall Singapore average of <span class="regionValues">{{SGoldAgeGroupRate}}%</span>.
            </span>

            <span v-else>
                It also has a younger population with <span class="regionValues">{{selectedRegionoldAgeGroupRate[0]}}%</span> who are 60 years old and above, compared to the overall Singapore average of <span class="regionValues">{{SGoldAgeGroupRate}}%</span>.
            </span>
            
            <br/><br/>
        </div>

        <!-- 2 regions are selected -->
        <div v-if="selectedRegions.length === 2">
            <span v-if="selectedRegionHighIncomeRate[0] > selectedRegionHighIncomeRate[1]">
                <span class="regionName">{{selectedRegions[0]}}</span> has a higher percentage of individual high income earners at <span class="regionValues">{{selectedRegionHighIncomeRate[0]}}%</span> compared to <span class="regionName">{{selectedRegions[1]}}</span> at <span class="regionValues">{{selectedRegionHighIncomeRate[1]}}%</span>.
            </span>

            <span v-else>
                <span class="regionName">{{selectedRegions[1]}}</span> has a higher percentage of individual high income earners at <span class="regionValues">{{selectedRegionHighIncomeRate[1]}}%</span> compared to <span class="regionName">{{selectedRegions[0]}}</span> at <span class="regionValues">{{selectedRegionHighIncomeRate[0]}}%</span>.
            </span>

            <span v-if="selectedRegionoldAgeGroupRate[0] > selectedRegionoldAgeGroupRate[1]">
                <span class="regionName">{{selectedRegions[0]}}</span> has an older population with <span class="regionValues">{{selectedRegionoldAgeGroupRate[0]}}%</span> who are 60 years old and above, compared to <span class="regionName">{{selectedRegions[1]}}</span> at <span class="regionValues">{{selectedRegionoldAgeGroupRate[1]}}%</span>.
            </span>

            <span v-else>
                <span class="regionName">{{selectedRegions[1]}}</span> has an older population with <span class="regionValues">{{selectedRegionoldAgeGroupRate[1]}}%</span> who are 60 years old and above, compared to <span class="regionName">{{selectedRegions[0]}}</span> at <span class="regionValues">{{selectedRegionoldAgeGroupRate[0]}}%</span>.
            </span>
            
            <br/><br/>
        </div>

        <!-- >2 regions are selected -->
        <div v-if="selectedRegions.length > 2">
            <span class="regionName">{{selectedRegions[highestIncomeIndex]}}</span> has the highest percentage of individual high income earners at <span class="regionValues">{{selectedRegionHighIncomeRate[highestIncomeIndex]}}%</span>, compared to
            <span v-for="(region, i) in selectedRegions" :key="i">
                <span v-if="i !== highestIncomeIndex">
                    <span v-if="(i === selectedRegions.length - 1) && (highestIncomeIndex !== selectedRegions.length - 1)">
                        {{region}}.
                    </span>
                    <span v-else>
                        {{region}} and
                    </span>
                </span>
            </span>

            <span class="regionName">{{selectedRegions[highestAgeIndex]}}</span> has the highest percentage of individuals who are 60 years old and above at <span class="regionValues">{{selectedRegionHighIncomeRate[highestAgeIndex]}}%</span>, compared to
            <span v-for="(region, i) in selectedRegions" :key="i">
                <span v-if="i !== highestAgeIndex">
                    {{region}}
                </span>              
            </span>.
            <br/><br/>
        </div>
    </div>
     
</template>

<script>
export default {

    name: "onemap-summary",
    props: ["selectedRegions", "onemapSummaryData"],
    
    data() {
        return {

            SGhighIncomeRate: 0,
            selectedRegionHighIncomeRate: [],
            SGoldAgeGroupRate: 0,
            selectedRegionoldAgeGroupRate: [],
            highestIncomeIndex: 0,
            highestAgeIndex: 0

        }
    },

    mounted() {
        this.SGhighIncomeRate = this.onemapSummaryData["average"]['Income From Work']['Percentage High Income [10000+]']
        this.SGoldAgeGroupRate = this.onemapSummaryData["average"]['Population Age Group']['Percentage 60 and above']
        this.selectedRegions.forEach(region => {
            this.selectedRegionHighIncomeRate.push(parseFloat(this.onemapSummaryData[region.toLowerCase()]['Income From Work']['Percentage High Income [10000+]']))
            this.selectedRegionoldAgeGroupRate.push(parseFloat(this.onemapSummaryData[region.toLowerCase()]['Population Age Group']['Percentage 60 and above']))
        });
        this.highestIncomeIndex = this.selectedRegionHighIncomeRate.reduce((iMax, x, i, arr) => x > arr[iMax] ? i : iMax, 0);
        this.highestAgeIndex = this.selectedRegionoldAgeGroupRate.reduce((iMax, x, i, arr) => x > arr[iMax] ? i : iMax, 0);
    },
        
}

</script>

<style>
    .regionName {
        color:#215085;
        font-weight:700;
        font-size:20px;
        text-transform: capitalize;
    }

    .regionValues {
        color:#d29a42;
        font-weight:700;
        font-size:20px;
    }
</style>