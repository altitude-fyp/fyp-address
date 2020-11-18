<template>
    <div>

        <GmapMap
            :options=gmapOptions
            :center=center
            :zoom="11.8"
            style="min-width:100%; min-height: 600px;">

        </GmapMap>

    </div>
</template>

<script>

export default {
    
    data() {
        return {
            center: {lat:1.3521, lng:103.8198},

            gmapOptions: {
                zoomControl: true,
                mapTypeControl: false,
                scaleControl: false,
                streetViewControl: false,
                rotateControl: false,
                fullscreenControl: false,
                disableDefaultUi: false
            },

        }
    }

}

</script>