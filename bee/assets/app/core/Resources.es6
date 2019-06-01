window.User = {
  install(Vue, options) {
    const url = '/api/v1/usuarios/'
    Vue.prototype.User = Vue.prototype.Resource(url)
  }
}

window.Abelha = {
  install (Vue, options) {
    const url = '/api/v1/abelhas/'
    Vue.prototype.Abelha = Vue.prototype.Resource(url)
  }
}
