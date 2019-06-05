Vue.use(bootstrapVue)
Vue.use(VeeValidate, {
  locale: 'pt_BR'
})
Vue.use(VueLoading)
Vue.component('loading', VueLoading)

Vue.use(Resource)
Vue.use(User)
Vue.use(Abelha)
Vue.use(EspecieAbelha)
Vue.use(TipoAbelha)
Vue.use(PaisAbelha)
Vue.use(Aviso)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
