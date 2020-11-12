<template>
    <div>

        <v-card v-if=selectableFeatures>

            <v-row style="padding-top: 8px;" justify="center">

                <!-- Button to clear selections goes here -->
                <v-btn outlined
                    color="#004D8E"
                    class="mb-2"
                    depressed
                    @click=clearFilter()>
                    Clear Filter
                </v-btn>

            </v-row>

            <div class="filtersSection">
                <div v-for="category in selectableFeatures" :key=category.cateegory>

                    <div class="filtersSectionTag"> {{ category["category"] }} </div>

                    <div v-for="feature in category.features" :key=feature>
                        <v-list-item>

                                <v-checkbox
                                    color="primary"
                                    :label=capitalize(feature)
                                    :value=feature
                                    v-model=selectedFeatures
                                    @change=emit>

                                </v-checkbox>

                        </v-list-item>
                    </div>

                </div>
            </div>

        </v-card>

    </div>
</template>

<script>

export default {

    name: "feature-selection-panel",

    props: ["selectableFeatures", "initialSelectedFeatures"],

    data() {
        return {
            selectedFeatures: []
        }
    },

    mounted() {

        this.selectedFeatures = this.initialSelectedFeatures

    },

    methods: {

        emit() {
            // this function passes this.selectedFeatures into its parent component
            this.$emit("checkboxChange", this.selectedFeatures)
        },

        capitalize(string) {
            return string.slice(0,1).toUpperCase() + string.slice(1)
        },

        clearFilter() {
            this.selectedFeatures = []
        }

    }

}

</script>

<style>

.filtersSectionTag {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
    padding:0 16px 0 16px;
}

.filtersSection {
    overflow-y: scroll;
    height:600px;
}

</style>
