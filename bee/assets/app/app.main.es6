const router = new VueRouter({
  routes: [
    { path: '/', component: Vue.component('abelhas') },
    { path: '/nova/abelha/', component: Vue.component('abelha') }
  ]
})

const app = new Vue({
  el: '#app',
  delimiters: ['[[', ']]'],
  filters: {
    pretty: function(value) {
      return JSON.stringify(JSON.parse(value), null, 2);
    }
  },
  router
})
