<template>
    <Nuxt />
</template>

<style>
body {
    font-family: "Roboto", sans-serif;
    background: #f8f4fe url("../images/login_splash_bg.jpg") no-repeat center center fixed; 
    -webkit-background-size: cover;
    -moz-background-size: cover;
    -o-background-size: cover;
    background-size: cover;
}
.container {
    height:100%;
}
.row_splash {
    margin-top:50px;
    max-width: 520px;
}
.headline {
    font-size: 32px;
    font-weight: 700;
    line-height: 110%;
    color: #004D8E;
    margin-top: 30px;
    margin-bottom: 15px;
}
.subheadline {
    font-size: 18px;
    font-weight: 300;
    line-height: normal;
    color: #424242;
    margin-bottom: 30px;
}
.v-btn.save-btn {
    min-width: 120px;
    min-height: 45px;
    color: #fff;
    text-transform: none;
    font-weight: 700;
}
.v-text-field .v-input__control .v-input__slot {
    min-height: 50px !important;
    max-width: 420px !important;
    display: flex !important;
    align-items: center !important;
    background: #F9F9F9;
  }
</style>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Roboto");
</style>