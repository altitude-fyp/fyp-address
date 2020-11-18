<template>
    <v-container>

        <v-row>

            <!-- left panel -->
            <v-col cols=4>
                <v-card>
                    <v-container style="padding:24px">

                    <!-- market segmentation header goes here -->
                    <h2 style="color: #D9261C">
                        <v-icon>
                            mdi-filter
                        </v-icon>
                        Market Segmentation
                    </h2>

                    <!-- the following filter r in place message goes here -->
                    <v-card-title>
                        <span style="font-size:18px">Selected Filters:</span>
                    </v-card-title>

                    <v-card-subtitle>
                        Employment status: {{selectedEmploymentStatus}} <br>
                        Household income: {{selectedHouseholdMonthlyIncome}} <br>
                        Monthly income: {{selectedIncome}} <br>
                        Population age group: {{selectedPopulationAgeGroup}} <br>
                    </v-card-subtitle>

                    <br>

                    <v-btn style="color:#d9261c"
                        outlined
                        block
                        @click=resetAllFilters
                        >
                        Reset all filters
                    </v-btn>

                    </v-container>
                </v-card>
            </v-col>


            <!-- right panel -->
            <v-col cols=8>
                <v-card>
                    <v-container style="padding:24px">


                        <!-- Employment status -->
                        <v-card-title>
                            <span class="filterName">Employment status</span>
                        </v-card-title>

                        <v-btn-toggle style="width:100%" color="#d9261c" mandatory v-model=selectedEmploymentStatus>
                            <v-btn v-for="(option,i) in employmentStatusOptions" 
                                :key=i
                                :value=option
                                style="width:33.33333%"
                                >
                                {{option}}   
                            </v-btn>
                        </v-btn-toggle>


                        <br><br>

                        <!-- household monthly income -->
                        <v-card-title>
                            <span class="filterName">Household monthly income</span>
                        </v-card-title>

                        <v-btn-toggle style="width:100%" color="#d9261c" mandatory v-model=selectedHouseholdMonthlyIncome>
                            <v-btn v-for="(option,i) in householdMonthlyIncomeOptions" 
                                :key=i
                                :value=option
                                style="width:25%"
                                >
                                {{option}}   
                            </v-btn>
                        </v-btn-toggle>

                        <br><br>

                        <!-- Monthly income from work -->
                        <v-card-title>
                            <span class="filterName">Monthly income from work</span>
                        </v-card-title> 

                        <v-btn-toggle style="width:100%" color="#d9261c" mandatory v-model=selectedIncome>
                            <v-btn v-for="(option,i) in monthlyIncomeOptions" 
                                :key=i
                                :value=option
                                style="width:25%"
                                >
                                {{option}}   
                            </v-btn>
                        </v-btn-toggle>
 
                            
                        <br><br>

                        <!-- Population age group -->
                        <v-card-title>
                            <span class="filterName">Population age group</span>
                        </v-card-title>

                        <v-btn-toggle style="width:100%" color="#d9261c" mandatory v-model=selectedPopulationAgeGroup>
                            <v-btn v-for="(option,i) in populationAgeGroupOptions" 
                                :key=i
                                :value=option
                                style="width:20%"
                                >
                                {{option}}   
                            </v-btn>
                        </v-btn-toggle>

                        <br><br><br>

                        <v-btn style="color:#fff"
                            color="#D9261C"
                            depressed
                            large
                            block
                            @click=submit
                            >
                            <span style="font-size:17px">Filter data</span>
                        </v-btn>
                    </v-container>
                </v-card>
            </v-col>

        </v-row>
    </v-container>
</template>

<script>

export default {

    data() {
        return {

            selectedEmploymentStatus: "None",
            selectedHouseholdMonthlyIncome: "None",
            selectedIncome: "None",
            selectedPopulationAgeGroup: "None",

            employmentStatusOptions: ["None", "Employed", "Unemployed"],
            householdMonthlyIncomeOptions: ["None", "Low [0-5000]", "Middle [5000-10000]", "High [10000+]"],
            monthlyIncomeOptions: ["None", "Low [0-3000]", "Middle [3000-6000]", "High [6000+]"],
            populationAgeGroupOptions: ["None", "0-19", "20-39", "40-59", "60+"],
        }
    },

    methods: {

        resetAllFilters() {
            this.selectedEmploymentStatus ="None"
            this.selectedHouseholdMonthlyIncome = "None"
            this.selectedIncome ="None"
            this.selectedPopulationAgeGroup = "None"
        },


        submit() {
            // this function is called when the user clicks on the "Filter data" button
            let url = process.env.BACKEND + "/api/analytics/market_segment/"

            let data = {
                economic_status: this.selectedEmploymentStatus == "None" ? "" : this.selectedEmploymentStatus,
                household_monthly_income_work : this.selectedHouseholdMonthlyIncome == "None" ? "" : this.selectedHouseholdMonthlyIncome,
                income_from_work : this.selectedIncome == "None" ? "" : this.selectedIncome,
                population_age_group: this.selectedPopulationAgeGroup == "None" ? "" : this.selectedPopulationAgeGroup,
            }

            console.log(data)

            this.$axios.post(url, data).then(response => {
                if (response.data.status == "success") this.$emit("filteredRegionsDataReceived", response.data.regions)
                else console.log("failed")
            })

            window.scrollTo({
                top: 0,
                left: 0,
                behavior: 'smooth'
            });

            this.resetAllFilters()

        }

    },

}

</script>

<style scoped>
  .filterName {
    color:#464646;
    font-size:16px;
    font-weight:500;
    text-align:center;
  }
</style>