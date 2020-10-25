<template>
  <v-app style="padding-top: 50px">
    <v-card>
      <v-tabs
        background-color="grey lighten-4"
        dense
        vertical>
        <v-tab>
          REST APIs
        </v-tab>
        <v-tab>
          Status Codes (Pending)
        </v-tab>
        <v-tab>
          Response Formats
        </v-tab>
        <!--Documentation for #Option 1 goes here-->
        <v-tab-item>
          <v-card flat>
            <v-card-text>

              ELABORATE THE CODE BLAH BLAH HERE BLAH BLAH
              ELABORATE THE CODE BLAH BLAH HERE BLAH BLAH
              ELABORATE THE CODE BLAH BLAH HERE BLAH BLAH
              ELABORATE THE CODE BLAH BLAH HERE BLAH BLAH
              ELABORATE THE CODE BLAH BLAH HERE BLAH BLAH


              <!-- Code Tabs and Scripts are in here-->
              <v-tabs fixed-tabs>
                <v-tab>PYTHON</v-tab>
                <v-tab>CURL</v-tab>
                <v-tab>NODEJS</v-tab>

                <!-- Scripts are below-->
                <!--Python script goes here-->
                <v-tab-item>
                  <v-card flat
                          elevation="2"
                          outlined
                          shaped
                          tile>
                    <v-card-text>

                      <v-row>
                        <v-col cols="1"><p class="caption">1</p></v-col>
                        <v-col>
                          <pre v-highlightjs><code class="javascript">const s = new Date().toString()</code></pre>
                        </v-col>
                      </v-row>

                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!--CURL script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="plaintext">
1 const s = new Date().toString()
2 const s = new Date().toString()
3 const s = new Date().toString()
4 const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!-- NodeJS script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="javascript">const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>

              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH
              CONTINUE THE CODE BLAH BLAH HERE BLAH BLAH


            </v-card-text>
          </v-card>
        </v-tab-item>
        <!--Documentation for #Option 2 goes here-->
        <v-tab-item>
          <v-card flat>
            <v-card-text>


              <!-- Code Tabs and Scripts are in here-->
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
  def functionname():
    s = 4
    y = 8
    print(s*y)
              </code></pre>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!--CURL script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="plaintext">const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!-- NodeJS script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="javascript">const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>

            </v-card-text>
          </v-card>
        </v-tab-item>
        <!--Documentation for #Option 3 goes here-->
        <v-tab-item>
          <v-card flat>
            <v-card-text>


              <!-- Code Tabs and Scripts are in here-->
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
  def functionname():
    s = 4
    y = 8
    print(s*y)
              </code></pre>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!--CURL script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="plaintext">const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>

                <!-- NodeJS script goes here-->
                <v-tab-item>
                  <v-card flat>
                    <v-card-text>
                      <div>
              <pre v-highlightjs><code class="javascript">const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()
const s = new Date().toString()</code></pre>
                      </div>
                    </v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs>

            </v-card-text>
          </v-card>
        </v-tab-item>
      </v-tabs>
    </v-card>

  </v-app>
</template>


<script>
export default {
  name: "apidocs",
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
