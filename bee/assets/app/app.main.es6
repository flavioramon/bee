const router = new VueRouter({
  routes: [
    { path: '/', component: Vue.component('index') },
    { path: '/nova/abelha/', component: Vue.component('abelha') },
    { path: '/novo/aviso/', component: Vue.component('aviso') }
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
