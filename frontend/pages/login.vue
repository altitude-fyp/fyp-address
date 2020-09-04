<template>
  <v-container>
    <div class="container">
      <div class="row_splash">

        <!-- Logo -->
        <img src="../images/citi_logo.png" height="60"/>

        <!-- Headline & Sub-headline -->
        <p class="headline">Address Analytics Tool</p>
        <p class="subheadline">Hello world. The quick brown fox jumps over the lazy dog. This is just some dummy text.</p>

        <!-- Login Fields -->
        <v-text-field height="10" color="#004D8E" outlined placeholder="Email Address" />

        <v-text-field type="password" placeholder="Password" outlined color="#004D8E"/>

        <v-btn class="save-btn" color="#004D8E" large depressed @click="login">Sign In</v-btn>

      </div>
    </div>
  </v-container>
</template>

<script>
export default {
  layout: 'loginlayout',
}
</script>

<style scoped>
  .v-text-field .v-input__control .v-input__slot {
    min-height: 50px !important;
    max-width: 420px !important;
    display: flex !important;
    align-items: center !important;
    background: #F9F9F9;
  }
</style>