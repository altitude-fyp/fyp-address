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
                        Current filters:
                    </v-card-title>

                    <v-card-subtitle>
                        Employment status: {{selectedEmploymentStatus}} <br>
                        Household income: {{selectedHouseholdMonthlyIncome}} <br>
                        Monthly income: {{selectedIncome}} <br>
                        Population age group: {{selectedPopulationAgeGroup}} <br>
                    </v-card-subtitle>

                    <br>

                    <v-btn style="color:#D9261C"
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
                            Employment status
                        </v-card-title>

                        <v-btn-toggle style="width:100%" mandatory v-model=selectedEmploymentStatus>
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
                            Household monthly income
                        </v-card-title>

                        <v-btn-toggle style="width:100%" mandatory v-model=selectedHouseholdMonthlyIncome>
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
                            Monthly income from work
                        </v-card-title> 

                        <v-btn-toggle style="width:100%" mandatory v-model=selectedIncome>
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
                            Population age group
                        </v-card-title>

                        <v-btn-toggle style="width:100%" mandatory v-model=selectedPopulationAgeGroup>
                            <v-btn v-for="(option,i) in populationAgeGroupOptions" 
                                :key=i
                                :value=option
                                style="width:20%"
                                >
                                {{option}}   
                            </v-btn>
                        </v-btn-toggle>

                        <br><br><br><br>

                        <v-btn style="color:#D9261C"
                            outlined
                            block
                            @click=submit
                            >
                            Filter data
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

            this.resetAllFilters()

        }

    },

}

</script>