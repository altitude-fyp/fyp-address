<template>
     <!-- Code Tabs and Scripts are in here-->
  <div>
    <v-tabs fixed-tabs>
      <v-tab>PYTHON</v-tab>
      <v-tab>CURL</v-tab>
      <v-tab>NODEJS</v-tab>

      <!-- Scripts are below-->
      <!--Python script goes here-->
      <v-tab-item>
          <v-card flat>
          <v-card-text>
              <pre v-highlightjs><code class="python">
       import requests
       url = "{{this.API_URL}}{{this.endpoint}}/"
       payload  = {"{{this.type}}": "{{this.address}}"}
       response = requests.post(url, data = payload)
       print(response.text.encode('utf8'))
      </code></pre>
          </v-card-text>
          </v-card>
      </v-tab-item>

      <!--CURL script goes here-->
      <v-tab-item>
          <v-card flat>
          <v-card-text>
              <div>
      <pre v-highlightjs><code class="python">
       curl --location --head '{{this.API_URL}}{{this.endpoint}}' \
       --data-raw '{
           "{{this.type}}": "{{this.address}}",
       }'

      </code></pre>
              </div>
          </v-card-text>
          </v-card>
      </v-tab-item>

      <!-- NodeJS script goes here-->
      <v-tab-item>
          <v-card flat>
          <v-card-text>
              <div>
      <pre v-highlightjs><code class="javascript">
        var raw = "{"{{this.type}}": "{{this.address}}"}";
      
        var requestOptions = {
        method: 'HEAD',
        body: raw,
        redirect: 'follow'
        };
      
        fetch("{{this.API_URL}}{{this.endpoint}}", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
      </code></pre>
              </div>
          </v-card-text>
          </v-card>
      </v-tab-item>

    </v-tabs>
    <v-row style="padding-bottom: 10px;" justify="center">
      <v-btn
        outlined
        color="#004D8E"
        class="mb-2 sidebar"
        width="250"
        depressed
        @click=downloadData()>

        <v-icon style="margin-right:5px">
            mdi-download
        </v-icon>

        Download JSON
      </v-btn>
    </v-row>
  </div>
</template>


<script>
export default {
  name: "apiResultDocs",
  props: ["address","endpoint","type"],
  data() {
    return {
      API_URL: "https://lzl.blue"
    }
  },
  methods: {
    downloadData() {

      var url = this.API_URL + this.endpoint

      this.$axios.post(url, {[this.type]: this.address}).then((response) => {
          console.log(response)
          const data = JSON.stringify(response)
          const blob = new Blob([data], {type: 'text/plain'})
          const e = document.createEvent('MouseEvents'),
          a = document.createElement('a');
          a.download = "data.json";
          a.href = window.URL.createObjectURL(blob);
          a.dataset.downloadurl = ['text/json', a.download, a.href].join(':');
          e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
          a.dispatchEvent(e);    
      })
    }
  }
}
</script>

<style>

/*

Lightfair style (c) Tristian Kelly <tristian.kelly560@gmail.com>

*/

.hljs {
  display: block;
  overflow-x: auto;
  padding: 0.5em;
  background: #fff !important;
}

.hljs-name {
  color:#01a3a3 !important;
}

.hljs-tag,.hljs-meta {
  color:#778899 !important;
}

.hljs,
.hljs-subst {
  color: #444 !important;
}

.hljs-comment {
  color: #888888 !important;
}

.hljs-keyword,
.hljs-attribute,
.hljs-selector-tag,
.hljs-meta-keyword,
.hljs-doctag,
.hljs-name {
  font-weight: bold
}

.hljs-type,
.hljs-string,
.hljs-number,
.hljs-selector-id,
.hljs-selector-class,
.hljs-quote,
.hljs-template-tag,
.hljs-deletion {
  color: #4286f4 !important;
}

.hljs-title,
.hljs-section {
  color: #4286f4 !important;
  font-weight: bold
}

.hljs-regexp,
.hljs-symbol,
.hljs-variable,
.hljs-template-variable,
.hljs-link,
.hljs-selector-attr,
.hljs-selector-pseudo {
  color: #BC6060 !important;
}

.hljs-literal {
  color: #62bcbc !important;
}

.hljs-built_in,
.hljs-bullet,
.hljs-code,
.hljs-addition {
  color: #25c6c6 !important;
}

.hljs-meta-string {
  color: #4d99bf !important;
}

.hljs-emphasis {
  font-style: italic
}

.hljs-strong {
  font-weight: bold
}



/*!* Tomorrow Night Theme *!
!* http://jmblog.github.com/color-themes-for-google-code-highlightjs *!
!* Original theme - https://github.com/chriskempson/tomorrow-theme *!
!* http://jmblog.github.com/color-themes-for-google-code-highlightjs *!

!* Tomorrow Comment *!
.hljs-comment,
.hljs-quote {
  color: #969896;
}

!* Tomorrow Red *!
.hljs-variable,
.hljs-template-variable,
.hljs-tag,
.hljs-name,
.hljs-selector-id,
.hljs-selector-class,
.hljs-regexp,
.hljs-deletion {
  color: #cc6666;
}

!* Tomorrow Orange *!
.hljs-number,
.hljs-built_in,
.hljs-builtin-name,
.hljs-literal,
.hljs-type,
.hljs-params,
.hljs-meta,
.hljs-link {
  color: #de935f;
}

!* Tomorrow Yellow *!
.hljs-attribute {
  color: #f0c674;
}

!* Tomorrow Green *!
.hljs-string,
.hljs-symbol,
.hljs-bullet,
.hljs-addition {
  color: #b5bd68;
}

!* Tomorrow Blue *!
.hljs-title,
.hljs-section {
  color: #81a2be;
}

!* Tomorrow Purple *!
.hljs-keyword,
.hljs-selector-tag {
  color: #b294bb;
}

.hljs {
  display: block;
  overflow-x: auto;
  background: #1d1f21 !important;
  color: #c5c8c6;
  padding: 0.5em;
}

.hljs-emphasis {
  font-style: italic;
}

.hljs-strong {
  font-weight: bold;
}*/

</style>
