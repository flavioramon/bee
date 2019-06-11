Vue.use(bootstrapVue)
Vue.use(VeeValidate, {
  locale: 'pt_BR'
})
Vue.use(VueLoading)
Vue.component('loading', VueLoading)

Vue.use(Resource)
Vue.use(User)
Vue.use(Leitura)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
