Vue.use(bootstrapVue)
Vue.use(Resource)
Vue.use(User)
Vue.use(Abelha)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
