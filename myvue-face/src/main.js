import Vue from 'vue';
import App from '../App.vue';
import VueWebCam from 'vue-web-cam';

Vue.config.productionTip = false;

Vue.use(VueWebCam);

new Vue({
  render: (h) => h(App),
}).$mount('#app');
